import os

# app/gpt_service.py
def query_gpt(client, gpt_query):
    """
    Function to send a query to the GPT model.

    Args:
        client (OpenAI): The OpenAI client.
        gpt_query (str): The query for GPT.

    Returns:
        str: The response from GPT.
    """
    try:
        completion = client.chat.completions.create(
            model= os.getenv('GPT_MODEL'),
            messages=[{"role": "user", "content": gpt_query}],
        )

        return completion.choices[0].message.content
    except Exception as e:
        raise e
