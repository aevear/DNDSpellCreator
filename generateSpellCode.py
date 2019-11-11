# generateSpells

def importTextFiles(text):
    fi = open(text, 'r') #reads in the file that list the before/after file names
    spellData = fi.read().split("#") #reads in files
    spellData = spellData[1:]
    completeList = []

    for spell in spellData:
        internalSections = spell.split("\n")
        # Name
        name = internalSections[1]
        name = name[6:]
        # Level
        level = internalSections[2]
        level = level[7:]
        # Type
        type = internalSections[3]
        type = type[6:]
        # Classes
        classes = internalSections[4]
        classes = classes[9:].strip(" ")
        # Casting Time
        casting = internalSections[5]
        casting = casting[14:]
        # Range
        range = internalSections[6]
        range = range[7:]
        # Components
        components = internalSections[7]
        components = components[12:]
        # Concentration
        concentration = internalSections[8]
        concentration = concentration[15:]
        # Duration
        duration = internalSections[9]
        duration = duration[9:]
        # Duration
        description = internalSections[10]
        description = description[13:]

        totalSpellList = [name, level, type, classes, casting, range, components, concentration, duration, description]

        completeList.append(totalSpellList)

    return completeList

def makeHomebrery(group, spellList):
    with open(group + "HomebrerySpells.txt", "w") as myfile:
        myfile.write("New Spell List\n--------------------------\n\n")

    for spell in spellList:
        name = spell[0]
        level = spell[1]
        if level == "1":
            level = "1st"
        elif level == "2":
            level = "2nd"
        elif level == "3":
            level = "3rd"
        else:
            level = level + "th"
        type = spell[2]
        classes = spell[3]
        castTime = spell[4]
        range = spell[5]
        components = spell[6]
        concentration = spell[7]
        duration = spell[8]
        description = spell[9]

        with open(group + "HomebrerySpells.txt", 'a') as f:
            f.write("#### " + name + "\n")
            f.write("*" + level + "-level " + type + "*\n")
            f.write("___" + "\n")
            f.write("- **Classes:** " + classes + "\n")
            f.write("- **Casting Time:** " + castTime + "\n")
            f.write("- **Range:** " + range + "\n")
            f.write("- **Components:** " + components + "\n")
            if concentration == "yes":
                concentration = "Concentration, "
            else:
                concentration = ""
            f.write("- **Duration:** " + concentration + duration + "\n")
            f.write("\n")
            f.write(description)
            f.write("\n\n")

def makeApp(group, spellList):
    mainString = ""
    mainString = mainString + ("[{\"version\":\"3.1.5\"},{\"db\":\"14\"},{\"data\":[")

    for spell in spellList:
        name = spell[0]
        level = str(spell[1])
        type = spell[2]
        if level == "1":
            type = "1st level " + type
        elif level == "2":
            type = "2nd level " + type
        elif level == "3":
            type = "3rd level " + type
        elif level == "Cantrip":
            type = type + " Cantrip"
            level = "-1"
        else:
            type = level + "th level " + type
        classes = spell[3].replace(" ","")
        castTime = spell[4]
        range = spell[5]
        components = spell[6]
        concentration = spell[7]
        if concentration == "yes":
            concentration = "true"
        else:
            concentration = "false"
        duration = spell[8]
        description = spell[9].replace("%","</p><p>")

        mainString = mainString + ("{")
        mainString = mainString + ("\"id\":5,")
        mainString = mainString + ("\"name\":\"" + name + "\",")
        mainString = mainString + ("\"school\":\"" + type+ "\",")
        mainString = mainString + ("\"level\":\"" + level + "\",")
        mainString = mainString + ("\"casting_time\":\"" + castTime + "\",")
        mainString = mainString + ("\"range\":\"" + range + "\",")
        mainString = mainString + ("\"components\":\"" + components + "\",")
        mainString = mainString + ("\"duration\":\"" + duration + "\",")
        mainString = mainString + ("\"description\":\"<p>" + description + "</p>\",")
        mainString = mainString + ("\"description_high\":\"" + "" + "\",")
        mainString = mainString + ("\"book\":\"" + group + "\",")
        mainString = mainString + ("\"note\":\"" + "" + "\",")
        mainString = mainString + ("\"classes\":\"" + classes + "\",")
        mainString = mainString + ("\"concentration\":\"" + concentration + "\",")
        mainString = mainString + ("\"ritual\":\"" + "false" + "\",")
        mainString = mainString + ("\"sound\":\"" + "" + "\"")
        mainString = mainString + ("},")

    mainString = mainString[:-1]
    mainString = mainString + ("]}]")
    with open("spells-" + group, 'w') as f:
        f.write(mainString)


spellCompendiumList = ["EldritchMagicSpells.txt", "BloodMagicSpells.txt", "ExpandedMagicSpells.txt"]

for group in spellCompendiumList:
    completeList = importTextFiles(group)
    makeHomebrery(group, completeList)
    makeApp(group, completeList)
