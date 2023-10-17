CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "code": {
            "type": "integer"
        },
        "type": {
            "type": "string"
        },
        "message": {
            "type": "string"
        }
    },
    "required": [
        "code",
        "type",
        "message"
    ]
}
