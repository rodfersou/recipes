{
  description = "dev-environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/release-23.11";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, nixpkgs-unstable, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        unstable = nixpkgs-unstable.legacyPackages.${system};
      in with pkgs; rec {
        devShell = mkShell {
          name = "dev-environment";
          nativeBuildInputs = [
            bash
            python311
            unstable.isort
            unstable.mypy
            unstable.poetry
            unstable.pre-commit
            unstable.ruff
          ] ++ (
            if ("$INSIDE_DOCKER" != "true")
            then [
              entr
              flyctl
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
            if [[ $INSIDE_DOCKER != "true" ]]
            then
              export POETRY_VIRTUALENVS_IN_PROJECT="true"
            fi
            unset PYTHONPATH
            poetry env use ${python311.executable}
        
            export PATH="$PWD/.venv/bin:$PATH"
          '';
        };
      }
    );
}
