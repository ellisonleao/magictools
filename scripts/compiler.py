from json import loads

def fix_name(name: str) -> str:
  adjusted_name = name.replace("-", " ")
  adjusted_name = adjusted_name.replace("_", "/")
  adjusted_name = adjusted_name.title()
  adjusted_name = adjusted_name.replace("And", "and")

  return adjusted_name

def pricing_legend(pricing: str) -> str | None:
  return {
    "free": ":free:",
    "open": ":tada:",
    "paid": ":moneybag:",
    "freemium": ":money_with_wings:",
  }.get(pricing, None)

def compile_content(content) -> str:
  content_data = {
    "pricing": content.get("pricing", "unknown"),
    "name": content.get("name", "Unknown"),
    "link": content.get("link", ""),
    "description": content.get("description", "")
  }

  compiled_content = "- "
  content_data["pricing"] = content_data["pricing"].lower()
  
  if content_data["pricing"] != "unknown":
    compiled_content += f"{pricing_legend(content_data["pricing"])} "
  
  if content_data["link"]:
    compiled_content += f"[{content_data["name"]}]({content_data["link"]})"
  else:
    compiled_content += content_data["name"]

  if content_data["description"]:
    compiled_content += f" - {content_data["description"]}"

  return compiled_content

def compile_topic(section, topic) -> str:
  index_path = f"contents/{section}/{topic}.json"
  topic_data = {
    "name": topic,
    "description": "",
    "contents": []
  }

  with open(index_path, "r") as index_file:
    data = loads(index_file.read())

    topic_data["name"] = data.get("name", section)
    topic_data["description"] = data.get("description", "")
    topic_data["contents"] = data.get("contents", [])

  topic_data["contents"].sort(key=lambda x: x.get("name", "").lower())
  compiled_topic = f"### {topic_data["name"]}\n\n"
  
  if topic_data["description"]:
    compiled_topic += f"{topic_data["description"]}\n\n"
  
  for item in topic_data["contents"]:
    compiled_topic += compile_content(item) + "\n"

  return compiled_topic

def compile_section(section) -> str:
  index_path = f"contents/{section}/index.json"
  section_data = {
    "name": section,
    "description": "",
    "contents": []
  }

  with open(index_path, "r") as index_file:
    data = loads(index_file.read())

    section_data["name"] = data.get("name", section)
    section_data["description"] = data.get("description", "")
    section_data["contents"] = data.get("contents", [])

  section_data["name"] = fix_name(section_data["name"])
  compiled_section = f"## {section_data["name"]}\n\n"
  
  if section_data["description"]:
    compiled_section += f"> _{section_data["description"]}_\n\n"
  
  for topic in section_data["contents"]:
    compiled_section += compile_topic(section, topic) + "\n"
  
  compiled_section += "\n"
  return compiled_section

def compile_api() -> str:
  index_path = "contents/index.json"
  api_data = {
    "contents": []
  }

  with open(index_path, "r") as index_file:
    data = loads(index_file.read())
    api_data["contents"] = data.get("contents", [])

  compiled_api = ""
  for section in api_data["contents"]:
    compiled_api += compile_section(section)

  return compiled_api

def compile_section_toc(section: str) -> str:
  index_path = f"contents/{section}/index.json"
  section_data = {
    "contents": []
  }

  with open(index_path, "r") as index_file:
    data = loads(index_file.read())
    section_data["contents"] = data.get("contents", [])

  section_link = f"[{fix_name(section)}](#{section})"
  compiled_section_toc = f"- {section_link}\n"
  
  for topic in section_data["contents"]:
    hash_name = topic.replace("_", "")
    topic_name = fix_name(topic)
    compiled_section_toc += f"  - [{topic_name}](#{hash_name})\n"
  
  return compiled_section_toc

def compile_api_toc() -> str:
  index_path = "contents/index.json"
  api_data = {
    "contents": []
  }

  with open(index_path, "r") as index_file:
    data = loads(index_file.read())
    api_data["contents"] = data.get("contents", [])

  compiled_api_toc = "## Table of Contents\n\n"
  for section in api_data["contents"]:
    compiled_api_toc += compile_section_toc(section)

  return compiled_api_toc

def compile_readme() -> str:
  with open("templates/README.md", "r") as template_file:
    template = template_file.read()

    compiled_contents = compile_api()
    compiled_toc = compile_api_toc()

    template = template.replace("[[CONTENTS]]", compiled_contents)
    template = template.replace("[[TOC]]", compiled_toc)

    return template

if __name__ == "__main__":
  compiled_readme = compile_readme()
  with open("README.md", "w") as readme_file:
    readme_file.write(compiled_readme)
