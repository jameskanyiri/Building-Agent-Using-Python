from openai import OpenAI

client = OpenAI()

#Simple example using response api
response = client.responses.create(
    model="gpt-4o-mini",
    input="Write one sentence about Kenya"
)

#For convenience use the output_text which aggregate all the text into a single string
response.output_text

#It is not safe to think that the model output is present at
response.output[0].content[0].text


#Message roles anf instruction following
response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Respond in swahili",
    input="What is the capital city of Tanzania"
)

response.output_text


#Message formatting with markdown and XML
instructions = """
# Identity

You are coding assistant that helps enforce the use of snake case 
variables in JavaScript code, and writing code that will run in 
Internet Explorer version 6.

# Instructions

* When defining variables, use snake case names (e.g. my_variable) 
  instead of camel case names (e.g. myVariable).
* To support old browsers, declare variables using the older 
  "var" keyword.
* Do not give responses with Markdown formatting, just return 
  the code as requested.

# Examples

<user_query>
How do I declare a string variable for a first name?
</user_query>

<assistant_response>
var first_name = "Anna";
</assistant_response>

"""

response = client.responses.create(
    model="gpt-4o-mini",
    instructions=instructions,
    input="How do i declare a variable for a last name"
)

response.output_text


#Few shot learning
instructions = """
# Identity

You are a helpful assistant that labels short product reviews as 
Positive, Negative, or Neutral.

# Instructions

* Only output a single word in your response with no additional formatting
  or commentary.
* Your response should only be one of the words "Positive", "Negative", or
  "Neutral" depending on the sentiment of the product review you are given.

# Examples

<product_review id="example-1">
I absolutely love this headphones — sound quality is amazing!
</product_review>

<assistant_response id="example-1">
Positive
</assistant_response>

<product_review id="example-2">
Battery life is okay, but the ear pads feel cheap.
</product_review>

<assistant_response id="example-2">
Neutral
</assistant_response>

<product_review id="example-3">
Terrible customer service, I'll never buy from them again.
</product_review>

<assistant_response id="example-3">
Negative
</assistant_response>
"""


response = client.responses.create(
    model="gpt-4o-mini",
    instructions=instructions,
    input="I like the pen but it is not writing smoothly"
)

response.output_text