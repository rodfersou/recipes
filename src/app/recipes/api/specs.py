from app.recipes.models import Recipe
from app.recipes.api.models import RecipeAPI, RecipeAPIWithID


recipe_schema = Recipe.model_json_schema()
recipe_api_schema = RecipeAPI.model_json_schema()
recipe_api_with_id_schema = RecipeAPIWithID.model_json_schema()


create_recipe = {
  "definitions": {
    "Recipe": recipe_schema,
    "RecipeAPI": recipe_api_schema
  },
  "parameters": [
    {
      "name": "recipe", 
      "description": "Recipe", 
      "in": "body", 
      "required": True, 
      "schema": {
        "$ref": "#/definitions/RecipeAPI",
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Created Recipe",
      "schema": {
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          },
          "recipe": {
            "items": {
              "$ref": "#/definitions/Recipe",
            },
            "type": "array"
          }
        }
      }
    }
  }
}


list_recipes = {
  "definitions": {
    "RecipeAPIWithID": recipe_api_with_id_schema
  },
  "responses": {
    "200": {
      "description": "A list of Recipes",
      "schema": {
        "properties": {
          "recipes": {
            "items": {
              "$ref": "#/definitions/RecipeAPIWithID",
            },
            "type": "array"
          }
        }
      },
    }
  }
}


get_recipe = {
  "definitions": {
    "RecipeAPIWithID": recipe_api_with_id_schema
  },
  "parameters": [
    {
      "name": "recipe_id", 
      "description": "Recipe ID", 
      "in": "path", 
      "required": True, 
      "type": "int",
    }
  ],
  "responses": {
    "200": {
      "description": "Requested Recipe",
      "schema": {
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          },
          "recipe": {
            "items": {
              "$ref": "#/definitions/RecipeAPIWithID",
            },
            "type": "array"
          }
        }
      },
    }
  }
}


update_recipe = {
  "definitions": {
    "RecipeAPI": recipe_api_schema
  },
  "parameters": [
    {
      "name": "recipe_id", 
      "description": "Recipe ID", 
      "in": "path", 
      "required": True, 
      "type": "int",
    },
    {
      "name": "recipe", 
      "description": "Recipe", 
      "in": "body", 
      "required": True, 
      "schema": {
        "$ref": "#/definitions/RecipeAPI",
      }
    }
  ],
  "responses": {
    "200": {
      "description": "Recipe Updated",
      "schema": {
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          },
          "recipe": {
            "items": {
              "$ref": "#/definitions/RecipeAPI",
            },
            "type": "array"
          }
        }
      },
    }
  }
}


delete_recipe = {
  "parameters": [
    {
      "name": "recipe_id", 
      "description": "Recipe ID", 
      "in": "path", 
      "required": True, 
      "type": "int",
    }
  ],
  "responses": {
    "200": {
      "description": "Recipe Deleted",
      "schema": {
        "properties": {
          "message": {
            "title": "Message",
            "type": "string"
          }
        }
      },
    }
  }
}
