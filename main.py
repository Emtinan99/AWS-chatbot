import boto3
import json
import traceback

# Your Nova Premier inference profile ARN
MODEL_ARN = "arn:aws:bedrock:us-east-1:652615011303:inference-profile/us.amazon.nova-premier-v1:0"

# Initialize Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def ask_bedrock(prompt):
    body = {
        "schemaVersion": "messages-v1",
        "inferenceConfig": {
            "maxTokens": 512,
            "temperature": 0.3,
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": (
                            "You are RetailBot, a helpful 24/7 assistant for a retail business. "
                            "Always provide clear, concise, and customer-friendly answers. "
                            "Use the following store details:\n\n"
                            "- Store Hours: Mon–Sat 9am–9pm, Sun 10am–6pm\n"
                            "- Return Policy: Items can be returned within 30 days with receipt\n"
                            "- Free Shipping: Available for orders over $50\n"
                            "- Order Tracking: Customers can check order status online or provide order ID\n\n"
                            "If asked something unrelated to retail, politely redirect back to store topics.\n\n"
                            f"Customer question: {prompt}"
                        )
                    }
                ]
            }
        ]
    }

    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ARN,
            body=json.dumps(body)
        )
        raw_body = response["body"].read().decode("utf-8")
        result = json.loads(raw_body)

        if "output" in result and "message" in result["output"]:
            return result["output"]["message"]["content"][0]["text"]
        else:
            return None

    except Exception as e:
        print("❌ Error:", e)
        traceback.print_exc()
        return None


def main():
    print("🛍️ Retail FAQ Chatbot (type 'exit' to quit)\n")
    print("Try asking things like:")
    print("- What are your store hours?")
    print("- What is your return policy?")
    print("- Do you offer free shipping?")
    print("- Where is my order?\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            reply = ask_bedrock(user_input)
            if reply:
                print("RetailBot:", reply)
            else:
                print("RetailBot: Sorry, I couldn’t get an answer right now.")

        except KeyboardInterrupt:
            print("\n🛑 Interrupted. Exiting.")
            break


if __name__ == "__main__":
    main()
