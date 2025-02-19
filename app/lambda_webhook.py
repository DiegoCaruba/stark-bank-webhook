from .services.webhook import parse_event, handle_event


def lambda_handler(event, context):

    if event["requestContext"]["http"]["method"] != "POST":
        return {
                    "body": "invalid method",
                    "statusCode": 405,
            }


    if event["headers"].get("Content-Type") != "application/json":
        return {
                    "body": "invalid Content-Type, expected application/json",
                    "statusCode": 415,
                }
    
    
    event = parse_event(
        content = event["body"],
        signature = event["header"].get("Digital-Signature"),
    )

    print(f"[*] Got event: Subscription: {event.subscription}, Type: {event.log.type}")

    handle_event(event)

    return {"statusCode": 200, "body": "OK"}
