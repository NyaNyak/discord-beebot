import discord
import random

def filtering(message):
    manage = "์ํ์ฌ๋ ๐โจ์์ ๋งโจ๐์ ์ฌ์ฉํด๐ก์ฃผ์ธ์~!๐๐"
    return manage

def command():
    embed = discord.Embed(title=f"๋ช๋ น์ด ๋ชจ์", description="๊ฟ๋ฒ๋ด์ ํ์ฌ ์๋ ๊ธฐ๋ฅ๋ค์ ์ง์ํ๊ณ  ์์ต๋๋ค!", color=0xf3bb76)
    embed.set_thumbnail(url="https://mblogthumb-phinf.pstatic.net/MjAxODA1MTdfMjEx/MDAxNTI2NTQ3NTYzMDI0.GGFyQth1IVreeUdrVmYVopJlv8ZX2EsTQGqQ3h6ktjEg.r6jltvwy2lBUvB_Wh4M9xvxw-gwV4RHUR1AXSF-nqpMg.PNG.heekyun93/4fb137544b692e53.png?type=w800")
    embed.add_field(name=f"!์ ์ ", value="`!์ ์  ๋๋ค์ (ex. !์ ์  ๋นฝํ์ํ์ )`\nํด๋น ์ ์  ์ ๋ณด๋ฅผ ์นด๋ ํ์์ผ๋ก ๋ณผ ์ ์์ต๋๋ค", inline=False)
    embed.add_field(name=f"!์ฑํผ์ธ", value="`!์ฑํผ์ธ ๋ผ์ธ ์ด๋ฆ (ex. !์ฑํผ์ธ ํ ๊ฐ๋ )\n์ฑํผ์ธ๋ช์ ๋ฐ๋์ โป๊ณต๋ฐฑ์์ดโป ์๋ ฅํด์ฃผ์ธ์!\n์ฑํผ์ธ๋ช์ ์ค์ฌ์ ์๋ ฅํด๋ ๊ฒ์ ๊ฐ๋ฅํฉ๋๋ค.\n[์์]\n์์ฐ๋ ๋ฆฌ์จ ์(x) ์์ฐ๋ ๋ฆฌ์จ์(o) ์์ฐ์(o)`\nํด๋น ๋ผ์ธ์์ ์ฑํผ์ธ์ ์น๋ฅ  ํ๋ณธ,\nํํธ๋ฆฌ ์ ๋ณด๋ฅผ ๊ฒ์ํฉ๋๋ค.",
                    inline=False)
    embed.add_field(name="ใค", value="ใค", inline=True)
    embed.add_field(name=f"[๊ทธ ์ธ ์ธ๋ชจ ์์ด ๋ณด์ด์ง๋ง ์์ํ ๊ธฐ๋ฅ๋ค]", value="`์จ๊ฒจ์ง ๋ช๊ฐ์ง ์ด์คํฐ์๊ทธ๋ ๋ค!\nโป์ฑํ ์ค ์ฌํ ์์ค์ ์ญ์  ๋  ์ ์์ผ๋\n์ฃผ์ํด ์ฃผ์ธ์โป`", inline=False)
    embed.add_field(name=f"์ธ์ฌ", value="`!์๋ (ex. !์๋, !์๋ํ์ธ์)`\n๊ฟ๋ฒ๋ด์ด ์ธ์ฌ๋ฅผ ๋ฐ์์ค๋๋ค!", inline=False)
    embed.add_field(name=f"์์ฌ ๋ฉ๋ด ์ถ์ฒ", value="`!๋ฐฅ or !๋ฉ๋ด (ex. !๋ฐฅ, !๋ฉ๋ด ์ถ์ฒ์ข)`\n๋ญ ๋จน์์ง ๊ณ ๋ฏผ๋์๋์?\n์์ฌ๋ ๊ผญ ์ฑ๊ฒจ๋์ธ์!", inline=False)
    embed.add_field(name="ใค", value="ใค", inline=True)
    embed.set_footer(text="๋ฒ๊ทธ ์ ๋ณด ๋ฐ ๋ฌธ์\nhttps://github.com/NyaNyak/2021-OSS",
                     icon_url="https://mblogthumb-phinf.pstatic.net/MjAxODA1MTdfMjg5/MDAxNTI2NTQ3NTYzMDIz.awWFb8WW9qSk85krQsWf7GXGOShPNS5ilZyVOFyrbIUg.07pMLGfgYvN_IQPPn9JLBRRvVE8yMY_xiN4LzuIfElEg.PNG.heekyun93/4c7a1d3932a211fa.png?type=w800")
    return embed

def hello(message):
    sentence = ["์๋ํ์ธ์ ", "์ค๋๋ ์ข์ ํ๋ฃจ ๋์ธ์ ", "ํ์ธ๊ณ  ๊ฐํ ํ๋ฃจ! ", "๊ฑด๊ฐ ์กฐ์ฌํ์ธ์ ", "์์ฌ๋ ํ์จ๋์? "]
    i = random.randint(0, len(sentence)-1)
    return sentence[i]

def hey(message):
    embed = discord.Embed(title="")
    embed.set_image(url="https://mblogthumb-phinf.pstatic.net/MjAxODA1MTdfMjg5/MDAxNTI2NTQ3NTYzMDIz.awWFb8WW9qSk85krQsWf7GXGOShPNS5ilZyVOFyrbIUg.07pMLGfgYvN_IQPPn9JLBRRvVE8yMY_xiN4LzuIfElEg.PNG.heekyun93/4c7a1d3932a211fa.png?type=w800")
    return embed

def garen(message):
    embed = discord.Embed(title="")
    embed.set_image(url="https://w.namu.la/s/39d986b83774de090109bcbd0ecfdb983cc21cb29fb02fbdafbc1f8170e59d7c2dd34e70c826538e6cdd9265a9c6bd5460a09495d9623fb866dc515be68abd002b697ccc9c7c5c75f927ccc791c87c8d3d25b791fbc721dce46ff6c83dafb137")
    return embed

def meal(message):
    food = ["๋๊น์ค", "๊น๋ฐฅ", "ํ๋ฒ๊ฑฐ", "๋ณด์", "์ปต๋ผ๋ฉด", "์ผ๊ฐ๊น๋ฐฅ", "๋ก๋ณถ์ด", "์๊ผฌ์น", "์ง์ฅ๋ฉด",
            "ํ์คํ", "๋ฆฌ์กฐ๋", "์ผ๊ฒน์ด", "ํผ์", "์๋๊ตญ", "์นํจ", "์ด๋ฐฅ", "๋ผ๋ฉด", "๋ญ๊ฐ๋น", "์กฑ๋ฐ",
            "๊ฐ์ํ", "ํด์ฅ๊ตญ", "์๋๋ถ์ฐ๊ฐ", "์น๋งฅ", "๊น์น์ฐ๊ฐ", "๋ถ๋์ฐ๊ฐ", "๋น๋น๋ฐฅ", "๋ถ๊ณ ๊ธฐ", "๊ณฑ์ฐฝ",
            "์นผ๊ตญ์", "์ค๋ ํ", "๊ฐ๋น", "์ผ๊ณํ", "์๊ตฌ์ฐ", "๋๋ฉด", "์งฌ๋ฝ", "๊ฐ๋นํ", "์๋ฌ๋", "๋์๋ฝ",
            "ํ", "์๊ตญ์", "๋ง๋ผํ", "๋ฉ๋ฐ์๋ฐ", "๋ผ๋ฉ", "๋ฎ๋ฐฅ", "์ฐ๋", "๊น์น๋ณถ์๋ฐฅ", "์ค๋ฏ๋ผ์ด์ค", "์นด๋ ",
            "๋ง๋", "์๋์์น", "๋ญ๋ณถ์ํ", "์ ์ก๋ณถ์", "๋์ฅ์ฐ๊ฐ", "์ ์ง๊ตญ", "์ถ์ดํ", "์ก๊ฐ์ฅ", "์ค๋ธ์ค๋ธ",
            "๋ญ๋ฐ", "์ฐ๋ญ", "ํ ์คํธ", "๋ผ์ง๊ตญ๋ฐฅ", "์๋จธ๋ฆฌ๊ตญ๋ฐฅ"]
    i = random.randint(0, len(food)-1)
    return food[i]