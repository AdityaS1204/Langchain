from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal,Optional

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "a breif summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["negative", "positive"],
      "description": "return the sentiment of the review either negative, postive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros in a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons in a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "wrtie the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

    
    
structured_output = model.with_structured_output(json_schema)
    
result = structured_output.invoke("""The Samsung Galaxy S24 Ultra stands as one of the most refined Android smartphones available today. From the moment you hold it, the titanium frame gives off a premium and durable feel. The display is nothing short of stunning — a 6.8-inch Dynamic AMOLED that offers vibrant colors, sharp resolution, and visibility that remains excellent even under direct sunlight. Performance is equally impressive, powered by the latest Snapdragon chipset, making multitasking, gaming, and AI-powered features smooth and fast.

One of the most standout aspects of the device is its camera system. Whether it's capturing ultra-wide landscapes or zooming in at 100x, the results are consistently sharp and detailed. Samsung’s new AI editing tools also make post-processing more accessible than ever, letting users remove unwanted objects or enhance photos with just a few taps.

However, the phone isn't without its downsides. It is bulky and quite heavy, which might not appeal to everyone. The price tag is also steep, making it less accessible for the average buyer. Additionally, while the AI features are impressive, some feel a bit gimmicky or half-baked in daily use. There's also the fact that Samsung continues the trend of not including a charger in the box, which feels like a cost-cutting move disguised as sustainability.

Despite these minor drawbacks, the Galaxy S24 Ultra remains a top-tier device. It’s best suited for power users, tech enthusiasts, and content creators who want the absolute best from their smartphone. For others, especially those with recent models like the S23 Ultra, the upgrades may not feel essential.
- Reviewed by aditya singh
""")
    
print(result)