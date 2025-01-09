#prompt the user for the answer to the Great Question of Life, the Universe and Everything
answer = input(" the answer to the Great Question of Life, the Universe and Everything? ")

match answer.lower().strip():
      #output Yes if the user inputs 42 or forty-two or forty two
      case "42" | "forty-two" | "forty two":
          print("Yes")
      #Otherwise output No
      case _ :
          print("No")

# i used lower for case-insensitively
# strip to remove spaces before and after
