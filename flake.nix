{
  description = "dev-environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-23.11";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix.url = "github:nix-community/poetry2nix";
  };

  outputs = { self, nixpkgs, nixpkgs-unstable, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        unstable = nixpkgs-unstable.legacyPackages.${system}.extend poetry2nix.overlays.default;
      in with pkgs; rec {
        devShell = mkShell {
          name = "dev-environment";
          nativeBuildInputs = [
            python311
            unstable.poetry
            unstable.ruff
            unstable.mypy
          ] ++ (
            if ("$INSIDE_DOCKER" != "true")
            then [
              entr
              httpie
              jq
              lazygit
              ripgrep
              silver-searcher
              tmux
              tree
              xeus
            ] else [
            ]
          );
          shellHook = ''
            export POETRY_VIRTUALENVS_IN_PROJECT="true"
            unset PYTHONPATH
            poetry env use ${python311.executable}
        
            export PATH="$PWD/.venv/bin:$PATH"
          '';
        };
        packages.app = unstable.poetry2nix.mkPoetryApplication {
          projectDir = ./.;
          overrides = unstable.poetry2nix.defaultPoetryOverrides.extend(self: super: {
            flasgger = super.flasgger.overridePythonAttrs(old: {
              buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
            });
            icdiff = super.icdiff.overridePythonAttrs(old: {
              buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
            });
            beeprint = super.beeprint.overridePythonAttrs(old: {
              buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
            });
            pytest-beeprint = super.pytest-beeprint.overridePythonAttrs(old: {
              buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
            });
            pydantic-factories = super.pydantic-factories.overridePythonAttrs(old: {
              buildInputs = (old.buildInputs or [ ]) ++ [ super.poetry ];
            });
          });
        };
        defaultPackage = packages.app;
      }
    );
}
