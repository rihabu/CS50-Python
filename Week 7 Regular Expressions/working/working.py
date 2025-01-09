import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    if match:=re.search(r"^([0-9]{1,2})(?:(?::)([0-5][0-9]))? (AM|PM) (?:to|TO) ([0-9]{1,2})(?:(?::)([0-5][0-9]))? (AM|PM)$",s.strip()):
        h1=hours_format(match.group(1), match.group(3))
        h2=hours_format(match.group(4), match.group(6))
        m1, m2=minutes_format(match.group(2), match.group(5))
        return f"{h1}:{m1} to {h2}:{m2}"
    else:
        raise ValueError

def hours_format(h,t):
    if t=="PM"and h!="12":
        h=int(h)+12
    elif t=="AM"and h!="12":
        h=h.zfill(2)
    elif t=="AM" and h=="12":
        h="00"
    return h

def minutes_format(m1,m2):
    if m1==None and m2==None:
        m1="00"
        m2="00"
        return m1,m2
    else:
        return m1,m2

if __name__ == "__main__":
    main()
