# Enter your code here. Read input from STDIN. Print output to STDOUT
nLines = int(input())
css = ""
isInsideSelector = False

for i in range(0, nLines):
    css += input()

while True:
    idx = css.find("{")

    if idx == -1:
        break

    isInsideSelector = True
    css = css[idx + 1 :]

    idx = css.find("}")
    cssSelector = css[:idx]

    cssProperties = cssSelector.split(";")

    for cssProperty in cssProperties:
        propIdx = cssProperty.find(":")
        cssValue = cssProperty[propIdx:]

        while True:
            colorIdx = cssValue.find("#")

            if colorIdx == -1:
                break

            cssValue = cssValue[colorIdx + 1 :]

            colorSepIdx = cssValue.find(" ")
            colorParenthesesIdx = cssValue.find(")")
            colorCommaIdx = cssValue.find(",")

            if colorCommaIdx != -1:
                colorSepIdx = colorCommaIdx

            elif colorParenthesesIdx != -1:
                colorSepIdx = colorParenthesesIdx

            rgb = cssValue

            if colorSepIdx != -1:
                rgb = cssValue[:colorSepIdx]

            rgbLen = len(rgb)
            if rgbLen != 3 and rgbLen != 6:
                continue

            isValid = True
            for c in rgb:
                if c.isdigit():
                    continue

                if c.isalpha():
                    cLower = c.lower()

                    if cLower >= "a" and cLower <= "f":
                        continue

                isValid = False
                break

            if isValid:
                print("#" + rgb)
