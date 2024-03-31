from openai import OpenAI
api_key = "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"

client = OpenAI(api_key=api_key)
def generate_response(prompt):
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:socialbullyalert3:97z66Ua9",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content