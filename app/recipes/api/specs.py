from app.recipes.api.models import APIRequest, APIResponse, UpdateAPIRequest
from app.recipes.models import Recipe

recipe_schema = Recipe.model_json_schema()
api_request_schema = APIRequest.model_json_schema()
api_response_schema = APIResponse.model_json_schema()
update_api_request_schema = UpdateAPIRequest.model_json_schema()


create_recipe = {
    "definitions": {
        "Recipe": recipe_schema,
        "APIRequest": api_request_schema,
    },
    "parameters": [
        {
            "name": "recipe",
            "description": "Recipe",
            "in": "body",
            "required": "true",
            "schema": {
                "$ref": "#/definitions/APIRequest",
            },
        }
    ],
    "responses": {
        "200": {
            "description": "Created Recipe",
            "schema": {
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string",
                    },
                    "recipe": {
                        "items": {
                            "$ref": "#/definitions/Recipe",
                        },
                        "type": "array",
                    },
                }
            },
        }
    },
}


list_recipes = {
    "definitions": {
        "APIResponse": api_response_schema,
    },
    "responses": {
        "200": {
            "description": "A list of Recipes",
            "schema": {
                "properties": {
                    "recipes": {
                        "items": {
                            "$ref": "#/definitions/APIResponse",
                        },
                        "type": "array",
                    }
                }
            },
        }
    },
}


get_recipe = {
    "definitions": {
        "APIResponse": api_response_schema,
    },
    "parameters": [
        {
            "name": "recipe_id",
            "description": "Recipe ID",
            "in": "path",
            "required": "true",
            "type": "integer",
        }
    ],
    "responses": {
        "200": {
            "description": "Requested Recipe",
            "schema": {
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string",
                    },
                    "recipe": {
                        "items": {
                            "$ref": "#/definitions/APIResponse",
                        },
                        "type": "array",
                    },
                }
            },
        }
    },
}


update_recipe = {
    "definitions": {
        "UpdateAPIRequest": update_api_request_schema,
        "APIRequest": api_request_schema,
    },
    "parameters": [
        {
            "name": "recipe_id",
            "description": "Recipe ID",
            "in": "path",
            "required": "true",
            "type": "integer",
        },
        {
            "name": "recipe",
            "description": "Recipe",
            "in": "body",
            "required": "true",
            "schema": {
                "$ref": "#/definitions/UpdateAPIRequest",
            },
        },
    ],
    "responses": {
        "200": {
            "description": "Recipe Updated",
            "schema": {
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string",
                    },
                    "recipe": {
                        "items": {
                            "$ref": "#/definitions/APIRequest",
                        },
                        "type": "array",
                    },
                }
            },
        }
    },
}


delete_recipe = {
    "parameters": [
        {
            "name": "recipe_id",
            "description": "Recipe ID",
            "in": "path",
            "required": "true",
            "type": "integer",
        }
    ],
    "responses": {
        "200": {
            "description": "Recipe Deleted",
            "schema": {
                "properties": {
                    "message": {
                        "title": "Message",
                        "type": "string",
                    },
                }
            },
        }
    },
}
