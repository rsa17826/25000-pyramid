from misc import print, LLM, f
import re

llm = LLM()
res = llm(
    r"give me a list of 50 simple topics like food, clothing, transportation, ect., that have common related words, just give the topics"
)
print(res)


def parseList(data):
    l = []
    for item in list(
        filter(lambda x: ((x.count(" ") <= 3) and x) or ". " in x, data.split("\n"))
    ):
        item = re.sub(r"^.*\. +", "", item, flags=re.MULTILINE).strip()
        if not item:
            continue
        if re.match(r"[^a-zA-Z ]", item):
            continue
        l.append(item)
    return l


cats = parseList(res)

print(cats)
for cat in cats:
    llm.clear()
    res = llm.ask(
        f"generate a list of 50 common words related to the topic '{cat}', that could be easy enough to describe and guess joined by newlines"
    )
    f.write(f"./l/{cat}", "\n".join(parseList(res)))
# Get-Content hiking | Sort-Object -Unique | Set-Content hiking

# # Get all files in the current directory with no extension
# $files = Get-ChildItem -Path . -File | Where-Object { -not $_.Extension }

# # Loop through each file and apply the command
# foreach ($file in $files) {
#     # Read the content of the file, sort it uniquely, and write it back to the same file
#     Get-Content $file.FullName | Sort-Object -Unique | Set-Content $file.FullName
# }
