#==============================================================================
# ** Archipelago_RGSS3
#------------------------------------------------------------------------------
#  All lines of text that start with # are comments and aren't read as code.
#  They'll appear in GREEN in the RPGMaker VX Ace script editor.
#
#  This script uses archipelago_rb to allow RPGMaker VX Ace games to connect
#  to the Archipelago Multiworld System.
#
#  Make sure you read the documentation to learn how this works after you
#  set this up! (LINK HERE)
#
#  Credits:
#  Author: EggSlashEther
#       (contact@eggslashether.com)
#  Tester: Scrungip
#       (Discord: scrungip)
#  Archipelago: All of the wonderful developers, staff and players
#       (https://archipelago.gg/)
#  mkxp: Ancurio + everyone else who made commits over the years
#       (https://github.com/Ancurio/mkxp)
#  mkxp-z: All of the maintainers + Ancurio's Discord server
#       (https://github.com/mkxp-z/mkxp-z)
#==============================================================================
#==============================================================================
# ** SETUP
#------------------------------------------------------------------------------
#  Ignore me! I'm just importing required libraries. Go to CONFIGURATION!
#==============================================================================
#--------------------------------------------------------------------------
# * Add "Ruby" directory to load path and import archipelago_rb
#--------------------------------------------------------------------------
    ruby_directory = File.join(Dir.pwd, "Ruby")

    $:.push(ruby_directory) unless System.is_mac?

    if File.directory?(ruby_directory)
        Dir.glob(File.join(ruby_directory, '**', '*')).each do |path|
            $:.push(path) if File.directory?(path)
        end
    end

    require 'archipelago_rb'
    require 'io/console'
#==============================================================================
# ** CONFIGURATION
#------------------------------------------------------------------------------
#  This section allows you to configure basic facts about the game.
#  For simpler RPGMaker VX Ace games, you shouldn't have to delve deeper than
#  this section.
#==============================================================================
#--------------------------------------------------------------------------
# * Basic Details
#  '$archipelago_gamename' is the game name as it appears in your APWorld.
#  '$archipelago_items_handling' determines what items this client can handle.
#    * DEFAULT: Archipelago::ItemsHandlingFlags::REMOTE_ALL
#  '$load_autoconnect' determines if the game will automatically try to
#  reconnect to its multiworld when loading a save.
#    * DEFAULT: true
#--------------------------------------------------------------------------
    $archipelago_gamename = "Kroniki Elevena"
    $archipelago_items_handling = Archipelago::ItemsHandlingFlags::REMOTE_ALL
    $load_autoconnect = true
#--------------------------------------------------------------------------
# * Progressive Methods
#  This hash contains calls you want to make for progressive items.
#  Each key/value pair should be a symbol and an array of methods in
#  string form. Then, you invoke the method progressive(key) in the
#  receiveditems_methods hash below. Whenever that progressive(key) method
#  is called, it calls the next function in the array. Make sure your keys
#  in receiveditems_methods are escaped!
#  Example:
#   progressive_methods = {
#       sword: [
#           "$game_party.gain_item($data_items[1], 1)",
#           "$game_party.gain_item($data_items[2], 1)",
#           "$game_party.gain_item($data_items[3], 1)"
#       ],
#       wand_upgrade: [
#           "$game_party.gain_item($data_items[(4..6), 1])"
#       ]
#   }
#   receiveditem_methods = {
#       80001 => "progressive(:sword)"
#       80002 => "progressive(:wand_upgrade)"
#   }
#     * When ID 80001 is first received, trigger the first method in the
#     array, in this case granting 1 of Game Item ID 1.
#     * When ID 80001 is received again, the second method in the array
#     triggers, granting 1 of Game Item ID 2.
#     * When ID 80001 is received again again, trigger the third method
#     in the array, granting 1 of Game Item ID 3.
#     * Ranges within brackets (like in the section below) work too!
#     * Like with ID 80002, with Game Item IDs 4 through 6 when called
#     one, two and three times respectively.
#
#  Note: If you ever call a progressive method more times than there are
#  entries in its array, nothing will happen, so don't worry about it.
#  MAKE SURE YOU CALL THE PROGRESSIVE METHOD IN THE ReceivedItem Methods
#  SECTION!
#--------------------------------------------------------------------------
    progressive_methods = {
        # Put your methods here. See the above comment for expected format.
        # Make sure to put a comma after every entry, except the last!
    }
#--------------------------------------------------------------------------
# * ReceivedItem Methods
#  This hash contains the methods you want to call when this
#  client gets a ReceivedItem of a specific ID. This doesn't have to be
#  restricted to only game items! Here's some examples:
#  22111 => "$game_party.gain_item($data_items[11], 22)",
#   * Gives 22 of Item ID 11.
#  100..110 => "$game_party.gain_item($data_items[1], 2)",
#   * 100, 101, etc, 110 each give 2 of Item ID 1.
#  10001..10010 => "$game_party.gain_item($data_items[(1..10)], 1)",
#   * 10001 gives 1 of Item ID 1, 10002 gives 1 of Item ID 2, etc, until 10
#   * Ranges made this way must be in brackets () and both have the same size!
#   * You can include more than one range in the value string, in which case
#   * all ranges must be the same size.
#  33333 => "$game_party.add_actor(1)"
#   * Adds Actor ID 1 to your party.
#  42069 => "$game_variables[1] += 5"
#   * Adds 5 to the 1st game variable.
#  69420 => "SceneManager.goto(Scene_Gameover)"
#   * Triggers a game over.
#  100000..100003 => "progressive(:revolver)"
#   * Triggers the next method in the "revolver" progressive array.
#--------------------------------------------------------------------------
    receiveditem_methods = {
        # Put your methods here. See the above comment for expected format.
        # Make sure to put a comma after every entry, except the last!
        # If you defined any progressive methods, make sure you call them!

        
        # Characters
    213700000 => "$game_party.add_actor(2)",  # Cupcake
    213700001 => "$game_party.add_actor(3)",  # Plush Foxy
    213700002 => "$game_party.add_actor(4)",  # Turret
    213700003 => "$game_party.add_actor(5)",  # Zombie
    213700004 => "$game_party.add_actor(6)",  # Pająk
    213700005 => "$game_party.add_actor(7)",  # Chlebek
    213700006 => "$game_party.add_actor(8)",  # Galaretka
    213700007 => "$game_party.add_actor(9)",  # Hater
    213700008 => "$game_party.add_actor(10)", # Dip
    213700009 => "$game_party.add_actor(11)", # Bob's Brain
    213700010 => "$game_party.add_actor(12)", # Bóbr
    213700011 => "$game_party.add_actor(13)", # Mroklum
    213700012 => "$game_party.add_actor(14)", # Robopirat
    213700013 => "$game_party.add_actor(15)", # Worms
    213700014 => "$game_party.add_actor(16)", # Slender
    213700015 => "$game_party.add_actor(17)", # Dingle
    213700016 => "$game_party.add_actor(18)", # Chica
    213700017 => "$game_party.add_actor(19)", # SCP-173
    213700018 => "$game_party.add_actor(20)", # Blue Baby
    213700019 => "$game_party.add_actor(21)", # Alex
    213700020 => "$game_party.add_actor(22)", # Robopirat Ninja
    213700021 => "$game_party.add_actor(23)", # Andre
    213700022 => "$game_party.add_actor(24)", # Globox
    213700023 => "$game_party.add_actor(25)", # Android
    213700024 => "$game_party.add_actor(26)", # Specimen 2
    213700025 => "$game_party.add_actor(27)", # Baloon Boy
    213700026 => "$game_party.add_actor(28)", # Toy Bonnie
    213700027 => "$game_party.add_actor(29)", # Rayman
    213700028 => "$game_party.add_actor(30)", # Kao
    213700029 => "$game_party.add_actor(31)", # Boogeyman
    213700030 => "$game_party.add_actor(32)", # Spooky
    213700031 => "$game_party.add_actor(33)", # Freddy
    213700032 => "$game_party.add_actor(34)", # Złoty Freddy
    213700033 => "$game_party.add_actor(35)", # Phantom Foxy
    213700034 => "$game_party.add_actor(36)", # SCP-049
    213700035 => "$game_party.add_actor(37)", # Reflux
    213700036 => "$game_party.add_actor(38)", # Jeff
    213700037 => "$game_party.add_actor(39)", # Isaac
    213700038 => "$game_party.add_actor(40)", # Azazel
    213700039 => "$game_party.add_actor(41)", # Monstro II
    213700040 => "$game_party.add_actor(42)", # Brzytwobrody
    213700041 => "$game_party.add_actor(43)", # Fuckboy
    213700042 => "$game_party.add_actor(44)", # Purple Guy
    213700043 => "$game_party.add_actor(45)", # BB
    213700044 => "$game_party.add_actor(46)", # SCP-106
    213700045 => "$game_party.add_actor(47)", # Kukiełka
    213700046 => "$game_party.add_actor(48)", # Ultra Greed
    213700047 => "$game_party.add_actor(49)", # Anim
    213700048 => "$game_party.add_actor(50)", # Cat Mario
    213700049 => "$game_party.add_actor(51)", # Indiana
    213700050 => "$game_party.add_actor(52)", # Serek(Kapłan)
    213700051 => "$game_party.add_actor(53)", # Lara Croft
    213700052 => "$game_party.add_actor(54)", # Serek(Wsparcie)
    213700053 => "$game_party.add_actor(55)", # Kaktus mag
    213700054 => "$game_party.add_actor(58)", # Papyrus

    # Key Items
    213700055 => "$game_party.gain_item($data_items[1], 1)",  # Kontroler
    213700056 => "$game_party.gain_item($data_items[10], 1)", # Krótkofalówka
    213700057 => "$game_party.gain_item($data_items[3], 1)",  # Siekiera
    213700058 => "$game_party.gain_item($data_items[18], 1)", # Młotek
    213700059 => "$game_party.gain_item($data_items[21], 1)", # Karta klucz I
    213700060 => "$game_party.gain_item($data_items[22], 1)", # Karta klucz II
    213700061 => "$game_party.gain_item($data_items[23], 1)", # Karta klucz V
    213700062 => "$game_party.gain_item($data_items[46], 1)", # Przenośny teleport
    213700063 => "$game_party.gain_item($data_items[55], 1)", # Kartka papieru
    213700064 => "$game_party.gain_item($data_items[58], 1)", # Tajemnicza część
    213700065 => "$game_party.gain_item($data_items[62], 1)", # Buty Laury
    213700066 => "$game_party.gain_item($data_items[68], 1)", # Dysk do rzucania
    213700067 => "$game_party.gain_item($data_items[70], 1)", # Złoty klucz
    213700068 => "$game_party.gain_item($data_items[72], 1)", # Guziczek
    213700069 => "$game_party.gain_item($data_items[73], 1)", # Ołówek i gumka
    213700070 => "$game_party.gain_item($data_items[74], 1)", # Antygrawitacyjne buty
    213700071 => "$game_party.gain_item($data_items[16], 1)", # Klucz

    # Quest Items
    213700072 => "$game_party.gain_item($data_items[4], 1)",  # Złoty grzyb
    213700073 => "$game_party.gain_item($data_items[20], 1)", # Sos grzybowy

    # Fillers
    213700074 => "$game_party.gain_item($data_items[5], 1)",  # Jabłko
    213700075 => "$game_party.gain_item($data_items[6], 1)",  # Winoogrono
    213700076 => "$game_party.gain_item($data_items[7], 1)",  # Mandarynka
    213700077 => "$game_party.gain_item($data_items[8], 1)",  # Wiśnie
    213700078 => "$game_party.gain_item($data_items[9], 1)",  # Zioła
    213700079 => "$game_party.gain_item($data_items[12], 1)", # Czerwony lum
    213700080 => "$game_party.gain_item($data_items[13], 1)", # Niebieski lum
    213700081 => "$game_party.gain_item($data_items[14], 1)", # Żółty lum
    213700082 => "$game_party.gain_item($data_items[15], 1)", # Marchewka
    213700083 => "$game_party.gain_item($data_items[24], 1)", # Srebrny klucz # idk what to do with it or how many there are
    213700084 => "$game_party.gain_item($data_items[25], 1)", # Pomidor
    213700085 => "$game_party.gain_item($data_items[26], 1)", # Koniczyna
    213700086 => "$game_party.gain_item($data_items[27], 1)", # Pikantna papryka
    213700087 => "$game_party.gain_item($data_items[44], 1)", # Cytryna
    213700088 => "$game_party.gain_item($data_items[45], 1)", # Wyciąg z kaktusa
    213700089 => "$game_party.gain_item($data_items[47], 1)",  # Penizol
    213700090 => "$game_party.gain_item($data_items[48], 1)", # Prezent
    213700091 => "$game_party.gain_item($data_items[49], 1)", # Mała ognista bomba
    213700092 => "$game_party.gain_item($data_items[50], 1)", # Duża ognista bomba
    213700093 => "$game_party.gain_item($data_items[51], 1)", # Mała wodna bomba
    213700094 => "$game_party.gain_item($data_items[52], 1)", # Duża wodna bomba
    213700095 => "$game_party.gain_item($data_items[53], 1)", # Mała ziemna bomba
    213700096 => "$game_party.gain_item($data_items[54], 1)", # Duża ziemna bomba
    213700097 => "$game_party.gain_item($data_items[57], 1)", # Smocza miłość
    213700098 => "$game_party.gain_item($data_items[59], 1)", # Meteoryt ataku
    213700099 => "$game_party.gain_item($data_items[60], 1)", # Meteoryt magii
    213700100 => "$game_party.gain_item($data_items[61], 1)", # Meteoryt szybkości
    213700101 => "$game_party.gain_item($data_items[63], 1)", # Mikstura zdrowia
    213700102 => "$game_party.gain_item($data_items[64], 1)", # Mikstura energii
    213700103 => "$game_party.gain_item($data_items[65], 1)", # Płynny szał
    213700104 => "$game_party.gain_item($data_items[66], 1)", # Gwiezdne Chrupki
    213700105 => "$game_party.gain_item($data_items[67], 1)", # Psia kupa
    213700106 => "$game_party.gain_item($data_items[69], 1)", # Kokarda Tarkopsa
    213700107 => "$game_party.gain_item($data_items[71], 1)",  # Płatek róży
    213700108 => "$game_party.gain_item($data_items[88], 1)",  # Płatek Tem
    213700109 => "$game_party.gain_item($data_items[89], 1)",  # Płatek Tem (wyprzedaż)
    213700110 => "$game_party.gain_item($data_items[90], 1)",  # Płatek Tem (zatruty)
    213700111 => "$game_party.gain_item($data_items[91], 1)", # Klejnot many
    213700112 => "$game_party.gain_item($data_items[92], 1)", # Klejnot cyberpunktów
    213700113 => "$game_party.gain_item($data_items[93], 1)", # Klejnot obrażeń
    213700114 => "$game_party.gain_item($data_items[94], 1)", # Klejnot życia
    213700115 => "$game_party.gain_item($data_items[95], 1)", # Klejnot ruchu
    213700116 => "$game_party.gain_item($data_items[96], 1)", # Olbrzymia ognista bomba
    213700117 => "$game_party.gain_item($data_items[97], 1)", # Gwiezdne Chrupki XL
    213700118 => "$game_party.gain_item($data_items[98], 1)", # Spaghetti
    213700119 => "$game_party.gain_item($data_items[99], 1)",  # Klejnot żywiołów
    213700120 => "$game_party.gain_item($data_items[101], 1)", # Babeczka

    # Key Items 2
    213700121 => "$game_party.gain_item($data_items[36], 1)", # Jad Venesosa Planta #idk how many

    # Key Items(Dwienków)
    213700122 => "$game_party.gain_item($data_items[37], 1)", # Świeczka
    213700123 => "$game_party.gain_item($data_items[38], 1)", # Info. o skrzyni
    213700124 => "$game_party.gain_item($data_items[39], 1)", # Info. o książkach
    213700125 => "$game_party.gain_item($data_items[40], 1)", # Info. o kominku
    213700126 => "$game_party.gain_item($data_items[41], 1)", # Materiał
    213700127 => "$game_party.gain_item($data_items[42], 1)", # Odcisk stopy
    213700128 => "$game_party.gain_item($data_items[43], 1)", # Info. o diamencie

    # Key Items(Snowdin)
    213700129 => "$game_party.gain_item($data_items[83], 1)", # Zeznania Blooka
    213700130 => "$game_party.gain_item($data_items[84], 1)", # Zeznania Snowdrake'a
    213700131 => "$game_party.gain_item($data_items[85], 1)", # Zielony materiał
    213700132 => "$game_party.gain_item($data_items[86], 1)", # Lodowy kolec
    213700133 => "$game_party.gain_item($data_items[87], 1)", # Miejsce zbrodni

    # Kapsuły
    213700134 => "$game_party.gain_item($data_items[28], 1)", # Kapsuła Plush Foxy'ego
    213700135 => "$game_party.gain_item($data_items[29], 1)", # Kapsuła Hatera
    213700136 => "$game_party.gain_item($data_items[30], 1)", # Kapsuła Dingle'a
    213700137 => "$game_party.gain_item($data_items[31], 1)", # Kapsuła Alex'a
    213700138 => "$game_party.gain_item($data_items[32], 1)", # Kapsuła Złotego Freddy'ego
    213700139 => "$game_party.gain_item($data_items[33], 1)", # Kapsuła Kangurka Kao
    213700140 => "$game_party.gain_item($data_items[34], 1)", # Kapsuła Fuckboy'a
    213700141 => "$game_party.gain_item($data_items[35], 1)", # Kapsuła Anima
    213700142 => "$game_party.gain_item($data_items[75], 1)", # Kapsuła Turreta
    213700143 => "$game_party.gain_item($data_items[76], 1)", # Kapsuła Mrokluma
    213700144 => "$game_party.gain_item($data_items[77], 1)", # Kapsuła Andre
    213700145 => "$game_party.gain_item($data_items[78], 1)", # Kapsuła Specimena 2
    213700146 => "$game_party.gain_item($data_items[79], 1)", # Kapsuła Foxy'ego
    213700147 => "$game_party.gain_item($data_items[80], 1)", # Kapsuła Jeffa
    213700148 => "$game_party.gain_item($data_items[81], 1)", # Kapsuła Kukiełki
    213700149 => "$game_party.gain_item($data_items[82], 1)", # Kapsuła Ultra Greeda

    # Key Items 3
    213700150 => "$game_party.gain_item($data_items[56], 1)", # Doggo
    213700151 => "$game_party.gain_item($data_items[102], 1)",# Różowe majciochy
    213700152 => "$game_party.gain_item($data_items[19], 1)", # Dusza
    213700153 => "$game_party.gain_item($data_items[17], 1)", # Diament

    # Armor
    213700154 => "$game_party.gain_item($data_armors[1], 1)", # "Niszczyciel"
    213700155 => "$game_party.gain_item($data_armors[2], 1)", # "Deska"
    213700156 => "$game_party.gain_item($data_armors[3], 1)", # "Wzmacniacz zdrowia"
    213700157 => "$game_party.gain_item($data_armors[4], 1)", # "Ubijaczka"
    213700158 => "$game_party.gain_item($data_armors[5], 1)", # "Kołdra"
    213700159 => "$game_party.gain_item($data_armors[6], 1)", # "Wspomagacz"

    213700160 => "$game_party.gain_item($data_armors[7], 1)", # Kask
    213700161 => "$game_party.gain_item($data_armors[8], 1)", # Drewniana tarcza
    213700162 => "$game_party.gain_item($data_armors[9], 1)", # Kapelusz
    213700163 => "$game_party.gain_item($data_armors[10], 1)", # Rubinowy naszyjnik
    213700164 => "$game_party.gain_item($data_armors[11], 1)", # Pelerynka
    213700165 => "$game_party.gain_item($data_armors[12], 1)", # Kapelusz wiedźmy
    
    213700166 => "$game_party.gain_item($data_armors[13], 1)", # "Wilcze szpony"
    213700167 => "$game_party.gain_item($data_armors[14], 1)", # "Wilcze futro"
    213700168 => "$game_party.gain_item($data_armors[15], 1)", # "Szczurzy ogon"
    213700169 => "$game_party.gain_item($data_armors[16], 1)", # "Złote pięści"
    213700170 => "$game_party.gain_item($data_armors[17], 1)", # "Różaniec"
    213700171 => "$game_party.gain_item($data_armors[18], 1)", # "Karta Mądrości"
    213700172 => "$game_party.gain_item($data_armors[19], 1)", # "Lewy but"
    213700173 => "$game_party.gain_item($data_armors[20], 1)", # "Czarna dziura"
    213700174 => "$game_party.gain_item($data_armors[21], 1)", # "Pistolet"
    213700175 => "$game_party.gain_item($data_armors[22], 1)", # "Błyskawica"
    213700176 => "$game_party.gain_item($data_armors[23], 1)", # "Głaz"
    213700177 => "$game_party.gain_item($data_armors[24], 1)", # "Kupa gruzu"
    213700178 => "$game_party.gain_item($data_armors[25], 1)", # "Toksyczna zbroja"
    213700179 => "$game_party.gain_item($data_armors[26], 1)", # "Dopalacz"
    213700180 => "$game_party.gain_item($data_armors[27], 1)", # "Kapelusz złodzieja"
    213700181 => "$game_party.gain_item($data_armors[28], 1)", # "Odnawiacz zdrowia I"
    
    213700182 => "$game_party.gain_item($data_armors[29], 1)", # Kamienna tarcza
    213700183 => "$game_party.gain_item($data_armors[30], 1)", # Drewniany puklerz
    213700184 => "$game_party.gain_item($data_armors[31], 1)", # Kamienny puklerz
    213700185 => "$game_party.gain_item($data_armors[32], 1)", # Peleryna
    213700186 => "$game_party.gain_item($data_armors[33], 1)", # Szata ciemności
    213700187 => "$game_party.gain_item($data_armors[34], 1)", # Szaty księcia
    213700188 => "$game_party.gain_item($data_armors[35], 1)", # Żelazne rękawice
    213700189 => "$game_party.gain_item($data_armors[36], 1)", # Mistyczny kapelusz
    213700190 => "$game_party.gain_item($data_armors[37], 1)", # Hełm rycerza
    213700191 => "$game_party.gain_item($data_armors[38], 1)", # Królicze uszy
    
    213700192 => "$game_party.gain_item($data_armors[39], 1)", # "Srebrny miecz"
    213700193 => "$game_party.gain_item($data_armors[40], 1)", # "Obieraczka"
    213700194 => "$game_party.gain_item($data_armors[41], 1)", # "Mistyczne ostrze"
    213700195 => "$game_party.gain_item($data_armors[42], 1)", # "Złoty łuk"
    213700196 => "$game_party.gain_item($data_armors[43], 1)", # "Różdżka"
    213700197 => "$game_party.gain_item($data_armors[44], 1)", # "Patyk"
    213700198 => "$game_party.gain_item($data_armors[45], 1)", # "Zachód słońca"
    213700199 => "$game_party.gain_item($data_armors[46], 1)", # "Gówniana tarcza"
    213700200 => "$game_party.gain_item($data_armors[47], 1)", # "Kartka papieru"
    213700201 => "$game_party.gain_item($data_armors[48], 1)", # "Narysowany pancerz"
    213700202 => "$game_party.gain_item($data_armors[49], 1)", # "Gówniany zapach"
    213700203 => "$game_party.gain_item($data_armors[50], 1)", # "Technologia"
    213700204 => "$game_party.gain_item($data_armors[51], 1)", # "Złote pióro"
    213700205 => "$game_party.gain_item($data_armors[52], 1)", # "Zajebisty but"
    213700206 => "$game_party.gain_item($data_armors[53], 1)", # "Armor mocy"
    213700207 => "$game_party.gain_item($data_armors[54], 1)", # "Karta Skilla I"
    
    213700208 => "$game_party.gain_item($data_armors[55], 1)", # Opaska bohatera
    213700209 => "$game_party.gain_item($data_armors[56], 1)", # Smoczy amulet
    213700210 => "$game_party.gain_item($data_armors[57], 1)", # Cegła
    213700211 => "$game_party.gain_item($data_armors[58], 1)", # Magiczna tarcza
    
    213700212 => "$game_party.gain_item($data_armors[59], 1)", # "Jopek"
    213700213 => "$game_party.gain_item($data_armors[60], 1)", # "Damka"
    213700214 => "$game_party.gain_item($data_armors[61], 1)", # "Król"
    213700215 => "$game_party.gain_item($data_armors[62], 1)", # "As"
    213700216 => "$game_party.gain_item($data_armors[63], 1)", # "Dzida"
    213700217 => "$game_party.gain_item($data_armors[64], 1)", # "Srebrna Dzida"
    213700218 => "$game_party.gain_item($data_armors[65], 1)", # "Złota Dzida"
    213700219 => "$game_party.gain_item($data_armors[66], 1)", # "Diamentowa Dzida"
    213700220 => "$game_party.gain_item($data_armors[67], 1)", # "Kubek Zdrowia"
    213700221 => "$game_party.gain_item($data_armors[68], 1)", # "Worek Zdrowia"
    213700222 => "$game_party.gain_item($data_armors[69], 1)", # "Wiadro Zdrowia"
    213700223 => "$game_party.gain_item($data_armors[70], 1)", # "Beczka zdrowia"
    213700224 => "$game_party.gain_item($data_armors[71], 1)", # "Skóra Knaarena"
    
    213700225 => "$game_party.gain_item($data_armors[72], 1)", # Mityczna Bransoleta
    213700226 => "$game_party.gain_item($data_armors[73], 1)", # Pokrywka
    213700227 => "$game_party.gain_item($data_armors[74], 1)", # Kawał metalu
    213700228 => "$game_party.gain_item($data_armors[75], 1)", # Skórzana czapa
    213700229 => "$game_party.gain_item($data_armors[76], 1)", # Czapka z daszkiem
    213700230 => "$game_party.gain_item($data_armors[77], 1)", # Plaster
    213700231 => "$game_party.gain_item($data_armors[78], 1)", # Opaska na oko
    213700232 => "$game_party.gain_item($data_armors[79], 1)", # Bocianie pióro
    213700233 => "$game_party.gain_item($data_armors[80], 1)", # Czapa mroku
    213700234 => "$game_party.gain_item($data_armors[81], 1)", # Naddźwiękowe buty
    213700235 => "$game_party.gain_item($data_armors[82], 1)", # Czterolistna koniczyna
    213700236 => "$game_party.gain_item($data_armors[83], 1)", # Teletarcza
    213700237 => "$game_party.gain_item($data_armors[84], 1)", # Aureola
    213700238 => "$game_party.gain_item($data_armors[85], 1)", # Amulet lodu
    213700239 => "$game_party.gain_item($data_armors[86], 1)", # Amulet ognia
    213700240 => "$game_party.gain_item($data_armors[87], 1)", # Amulet grzmotów
    213700241 => "$game_party.gain_item($data_armors[88], 1)", # Srebrna tarcza
    213700242 => "$game_party.gain_item($data_armors[89], 1)", # Pozłacana tarcza
    213700243 => "$game_party.gain_item($data_armors[90], 1)", # Zbroja rycerza
    213700244 => "$game_party.gain_item($data_armors[91], 1)", # Płynne szczęście
    
    213700245 => "$game_party.gain_item($data_armors[92], 1)", # "Petarda"
    213700246 => "$game_party.gain_item($data_armors[93], 1)", # "Dynamit"
    213700247 => "$game_party.gain_item($data_armors[94], 1)", # "Bomba"
    213700248 => "$game_party.gain_item($data_armors[95], 1)", # "Atomówka"
    213700249 => "$game_party.gain_item($data_armors[96], 1)", # "Patyczek"
    213700250 => "$game_party.gain_item($data_armors[97], 1)", # "Laska"
    213700251 => "$game_party.gain_item($data_armors[98], 1)", # "Złota laska"
    213700252 => "$game_party.gain_item($data_armors[99], 1)", # "Mistyczna różdżka"
    213700253 => "$game_party.gain_item($data_armors[100], 1)", # "Mieszaniec I"
    213700254 => "$game_party.gain_item($data_armors[101], 1)", # "Koszulka"
    213700255 => "$game_party.gain_item($data_armors[102], 1)", # "Koszula"
    213700256 => "$game_party.gain_item($data_armors[103], 1)", # "Kurtka"
    213700257 => "$game_party.gain_item($data_armors[104], 1)", # "Kombinezon"
    213700258 => "$game_party.gain_item($data_armors[105], 1)", # "Karta Skilla II"
    213700259 => "$game_party.gain_item($data_armors[106], 1)", # "Karta Skilla III"
    213700260 => "$game_party.gain_item($data_armors[107], 1)", # "Karta Skilla IV"
    213700261 => "$game_party.gain_item($data_armors[108], 1)", # "Wspomaganie kierownicy"
    213700262 => "$game_party.gain_item($data_armors[109], 1)", # "Okulary przeciwsłoneczne"
    213700263 => "$game_party.gain_item($data_armors[110], 1)", # "Respirator"
    
    213700264 => "$game_party.gain_item($data_armors[111], 1)", # Kocie uszy
    213700265 => "$game_party.gain_item($data_armors[112], 1)", # Czerwona suknia
    213700266 => "$game_party.gain_item($data_armors[113], 1)", # Płaszcz Gary'ego
    213700267 => "$game_party.gain_item($data_armors[114], 1)", # Smoczy hełm
    213700268 => "$game_party.gain_item($data_armors[115], 1)", # Smocza zbroja
    213700269 => "$game_party.gain_item($data_armors[116], 1)", # Szaty najwyższego maga
    213700270 => "$game_party.gain_item($data_armors[117], 1)", # Kamizelka kuloodporna
    213700271 => "$game_party.gain_item($data_armors[118], 1)", # Złota wstążka
    213700272 => "$game_party.gain_item($data_armors[119], 1)", # Maska karnawałowa
    213700273 => "$game_party.gain_item($data_armors[120], 1)", # Tarcza policyjna
    
    213700274 => "$game_party.gain_item($data_armors[121], 1)", # "Brązowa wstążka"
    213700275 => "$game_party.gain_item($data_armors[122], 1)", # "Srebrna wstążka"
    213700276 => "$game_party.gain_item($data_armors[123], 1)", # "Złota wstążka"
    213700277 => "$game_party.gain_item($data_armors[124], 1)", # "Legendarna wstążka"
    213700278 => "$game_party.gain_item($data_armors[125], 1)", # "Brązowa tarcza"
    213700279 => "$game_party.gain_item($data_armors[126], 1)", # "Srebrna tarcza"
    213700280 => "$game_party.gain_item($data_armors[127], 1)", # "Złota tarcza"
    213700281 => "$game_party.gain_item($data_armors[128], 1)", # "Legendarna tarcza"
    213700282 => "$game_party.gain_item($data_armors[129], 1)", # "zBrOjA v 0.1"
    213700283 => "$game_party.gain_item($data_armors[130], 1)", # "zBrOjA v 0.2"
    213700284 => "$game_party.gain_item($data_armors[131], 1)", # "zBrOjA v 0.3"
    213700285 => "$game_party.gain_item($data_armors[132], 1)", # "zBrOjA v 0.4"
    213700286 => "$game_party.gain_item($data_armors[133], 1)", # "Miseczka"
    213700287 => "$game_party.gain_item($data_armors[134], 1)", # "Miska"
    213700288 => "$game_party.gain_item($data_armors[135], 1)", # "Micha"
    213700289 => "$game_party.gain_item($data_armors[136], 1)", # "Wanna"
    213700290 => "$game_party.gain_item($data_armors[137], 1)", # "Dyskietka"
    213700291 => "$game_party.gain_item($data_armors[138], 1)", # "Płyta"
    213700292 => "$game_party.gain_item($data_armors[139], 1)", # "Dysk"
    213700293 => "$game_party.gain_item($data_armors[140], 1)", # "Chmura"
    213700294 => "$game_party.gain_item($data_armors[141], 1)", # "Stojak"
    213700295 => "$game_party.gain_item($data_armors[142], 1)", # "Statyw"
    213700296 => "$game_party.gain_item($data_armors[143], 1)", # "Mikrofon"
    213700297 => "$game_party.gain_item($data_armors[144], 1)", # "Megafon"
    213700298 => "$game_party.gain_item($data_armors[146], 1)", # "Karta Skilla V"
    213700299 => "$game_party.gain_item($data_armors[147], 1)", # "Pierścień śmierci"
    
    213700300 => "$game_party.gain_item($data_armors[148], 1)", # Brelok żywiołu ognia
    213700301 => "$game_party.gain_item($data_armors[149], 1)", # Brelok żywiołu lodu
    213700302 => "$game_party.gain_item($data_armors[150], 1)", # Brelok żywiołu błyskawicy
    213700303 => "$game_party.gain_item($data_armors[151], 1)", # Głowa Bendy'ego
    213700304 => "$game_party.gain_item($data_armors[152], 1)", # "Armor do bicia kobiet" # 1 or 2 or 4
    213700305 => "$game_party.gain_item($data_armors[153], 1)", # Brelok z Gacusiem
    
    # Tem armor
    213700306 => "$game_party.gain_item($data_armors[145], 1)", # Tem armor # will a be setting

    # Weapons
    213700307 => "$game_party.gain_item($data_weapons[1], 1)",  # Zardzewiały miecz
    213700308 => "$game_party.gain_item($data_weapons[2], 1)",  # Tępy nożyk
    213700309 => "$game_party.gain_item($data_weapons[3], 1)",  # Drewniana różdżka
    213700310 => "$game_party.gain_item($data_weapons[4], 1)",  # Używane rękawice
    213700311 => "$game_party.gain_item($data_weapons[5], 1)",  # Ostry nożyk
    213700312 => "$game_party.gain_item($data_weapons[6], 1)",  # Używany miecz
    213700313 => "$game_party.gain_item($data_weapons[7], 1)",  # Kradziona różdżka
    213700314 => "$game_party.gain_item($data_weapons[8], 1)",  # Rękawice
    213700315 => "$game_party.gain_item($data_weapons[9], 1)",  # Lodołamacz
    213700316 => "$game_party.gain_item($data_weapons[10], 1)", # Lekki nóż
    213700317 => "$game_party.gain_item($data_weapons[11], 1)", # Rękawiczki
    213700318 => "$game_party.gain_item($data_weapons[12], 1)", # Patyk do hipnozy
    213700319 => "$game_party.gain_item($data_weapons[13], 1)", # Maczuga
    213700320 => "$game_party.gain_item($data_weapons[14], 1)", # Pochodnia
    213700321 => "$game_party.gain_item($data_weapons[15], 1)", # Ostrze ciemności
    213700322 => "$game_party.gain_item($data_weapons[16], 1)", # Zatrute ostrze
    213700323 => "$game_party.gain_item($data_weapons[17], 1)", # Wodna różdżka
    213700324 => "$game_party.gain_item($data_weapons[18], 1)", # Laska mocy
    213700325 => "$game_party.gain_item($data_weapons[19], 1)", # Magiczne rękawice
    213700326 => "$game_party.gain_item($data_weapons[20], 1)", # Antyczne rękawiczki
    213700327 => "$game_party.gain_item($data_weapons[21], 1)", # Halabarda
    213700328 => "$game_party.gain_item($data_weapons[22], 1)", # Trujący miecz
    213700329 => "$game_party.gain_item($data_weapons[23], 1)", # Zestaw Rycerza
    213700330 => "$game_party.gain_item($data_weapons[24], 1)", # Srebrny miecz
    213700331 => "$game_party.gain_item($data_weapons[25], 1)", # Różdżka grzmotu
    213700332 => "$game_party.gain_item($data_weapons[26], 1)", # Kij Wielkiego Maga
    213700333 => "$game_party.gain_item($data_weapons[27], 1)", # PARALIZATOR
    213700334 => "$game_party.gain_item($data_weapons[28], 1)", # Wyważona laska
    213700335 => "$game_party.gain_item($data_weapons[29], 1)", # Skórzane rękawice
    213700336 => "$game_party.gain_item($data_weapons[30], 1)", # Dziurawe Rękawiczki
    213700337 => "$game_party.gain_item($data_weapons[31], 1)", # Kastet
    213700338 => "$game_party.gain_item($data_weapons[32], 1)", # Pozłacane Rękawice
    213700339 => "$game_party.gain_item($data_weapons[33], 1)", # Srebrny nóż
    213700340 => "$game_party.gain_item($data_weapons[34], 1)", # Wodny nożyk
    213700341 => "$game_party.gain_item($data_weapons[35], 1)", # Noże do rzucania
    213700342 => "$game_party.gain_item($data_weapons[36], 1)", # Ostrze ognia
    213700343 => "$game_party.gain_item($data_weapons[37], 1)", # Pędzel Guerteny
    213700344 => "$game_party.gain_item($data_weapons[38], 1)", # Nóż malarski
    213700345 => "$game_party.gain_item($data_weapons[39], 1)", # Szabla
    213700346 => "$game_party.gain_item($data_weapons[40], 1)", # Ostrze barbarzyńcy
    213700347 => "$game_party.gain_item($data_weapons[41], 1)", # Kosa śmierci
    213700348 => "$game_party.gain_item($data_weapons[42], 1)", # Rubinowa różdżka
    213700349 => "$game_party.gain_item($data_weapons[43], 1)", # Trójząb
    213700350 => "$game_party.gain_item($data_weapons[44], 1)", # Berło śmierci
    213700351 => "$game_party.gain_item($data_weapons[45], 1)", # Rękawice kuchenne
    213700352 => "$game_party.gain_item($data_weapons[46], 1)", # Rękawice z brązu
    213700353 => "$game_party.gain_item($data_weapons[47], 1)", # Rękawice śmierci
    213700354 => "$game_party.gain_item($data_weapons[48], 1)", # Tasak
    213700355 => "$game_party.gain_item($data_weapons[49], 1)", # Ostrze mrozu
    213700356 => "$game_party.gain_item($data_weapons[50], 1)", # Klinga śmierci
    # Dark Eleven
    213700357 => "$game_party.gain_item($data_weapons[51], 1)", # Miecz Dark Elevena
    213700358 => "$game_party.gain_item($data_weapons[52], 1)", # Ostrze Dark Elevena
    213700359 => "$game_party.gain_item($data_weapons[53], 1)", # Laska Dark Elevena
    213700360 => "$game_party.gain_item($data_weapons[54], 1)", # Kastet Dark Elevena
    
    # Variables & Switches
    # Temmie
    213700361 => "$game_variables[89] += 1",
    213700362 => "$game_variables[89] += 1",
    213700363 => "$game_variables[89] += 1",
    213700364 => "$game_variables[89] += 1",
    213700365 => "$game_variables[89] += 1",
    213700366 => "$game_variables[89] += 1",
    213700367 => "$game_variables[89] += 1",
    213700368 => "$game_variables[89] += 1",
    213700369 => "$game_variables[89] += 1",
    213700370 => "$game_variables[89] += 1",
    # Doors
    213700371 => "$game_switches[142] = true", # FNaF
    213700372 => "$game_switches[292] = true", # Sklep pierwsze miasto
    


    # Ładunki mocy # Idk how many 
    75678600 => "$game_variables[87] += 1",
    # 75678601 => "$game_variables[87] += 1",
    # 75678602 => "$game_variables[87] += 1",
    # 75678603 => "$game_variables[87] += 1",
    # 75678604 => "$game_variables[87] += 1",
    # 75678605 => "$game_variables[87] += 1",
    # 75678606 => "$game_variables[87] += 1",
    # 75678607 => "$game_variables[87] += 1",
    # 75678608 => "$game_variables[87] += 1",
    # 75678609 => "$game_variables[87] += 1",
    # 75678610 => "$game_variables[87] += 1",














    # Other Items
    #213700071 => "$game_party.gain_item($data_items[100], 1)",# Diamentowy pierścionek
    #213700071 => "$game_party.gain_item($data_items[11], 1)", # Krótkofalówka(Only in battle) i think it's not needed
    #213700071 => "$game_party.gain_item($data_items[17], 5)", # Diament
    #213700071 => "$game_party.gain_item($data_items[19], 2)", # Dusza
    #213700071 => "$game_party.gain_item($data_items[102], 1)",  # Neskot
    #213700151 => "$game_party.gain_item($data_items[2], 1)",  # Telefon i think it is better to not incluude it


    
    }
#==============================================================================
# ** ADVANCED
#------------------------------------------------------------------------------
#  For more complicated games - or more advanced users - additional options
#  are provided here to further customize how this integration works.
#==============================================================================
#--------------------------------------------------------------------------
# * There are currently no advanced settings.
#--------------------------------------------------------------------------
#==============================================================================
# ** CODE
#------------------------------------------------------------------------------
#  The feeble should not proceed past this point. Here be dragons.
#==============================================================================
#--------------------------------------------------------------------------
# * Method: Get ranges from string
#--------------------------------------------------------------------------
    def get_rng_from_str(string)
        range_regex = /\((\d+)(\.{2,3})(\d+)\)/
                ranges = []

        string.scan(range_regex) do |match|
            start_value = match[0].to_i
            end_value = match[2].to_i
            inclusive = match[1] == '..'
            ranges << (inclusive ? (start_value..end_value) : (start_value...end_value))
        end

        ranges.empty? ? false : ranges
    end
#--------------------------------------------------------------------------
# * Method: Replace all ranges in string with placeholder
#--------------------------------------------------------------------------
    def replace_rng_with_pl(string)
        range_regex = /\((\d+)(\.{2,3})(\d+)\)/

                ranges = string.scan(range_regex)
        string = string.gsub(range_regex, "\uFFFC") if ranges.any?

        return string
    end
#--------------------------------------------------------------------------
# * Method: Replace all placeholders in string with integers
#--------------------------------------------------------------------------
    def replace_pl_with_int(string, ints)
        i = -1

        modified_string = string.gsub(/\uFFFC/) do |match|
            i += 1
            ints[i]
        end

        return modified_string
    end
#--------------------------------------------------------------------------
# * Method: Expand Progressive methods into new hash (with arrays)
#--------------------------------------------------------------------------
    def expand_progressive_methods(progressive_methods)
        expanded_progressive_methods = {}

        progressive_methods.each do |key, value|
            iterate_to = 0
            pro_method_array = []
            value.each do |pro_method|
                ranges = get_rng_from_str(pro_method)
                if ranges
                    modding_string = replace_rng_with_pl(pro_method)
                    ranges.each do |range|
                        iterate_to = range.to_a.length if (iterate_to == 0) || (range.to_a.length < iterate_to)
                    end
                    iterate_to.times do |i|
                        ints_to_add = []
                        ranges.each do |range|
                            ints_to_add << (range.to_a[i])
                        end
                        modded_string = replace_pl_with_int(modding_string, ints_to_add)
                        pro_method_array << modded_string
                    end
                else
                    pro_method_array << pro_method
                end
            end
            expanded_progressive_methods[key] = pro_method_array
        end

        return expanded_progressive_methods
    end
#--------------------------------------------------------------------------
# * Method: Expand ReceivedItem methods into new hash
#--------------------------------------------------------------------------
    def expand_receiveditem_methods(receiveditem_methods)
        expanded_receiveditem_methods = {}

        receiveditem_methods.each do |key, value|
            if key.is_a?(Range)
                ranges = get_rng_from_str(value)
                if ranges
                    modding_string = replace_rng_with_pl(value)
                    key.each_with_index do |v, i|
                        ints_to_add = []
                        ranges.each do |range|
                            ints_to_add << (range.to_a[i])
                        end
                        modded_string = replace_pl_with_int(modding_string, ints_to_add)
                        expanded_receiveditem_methods[v] = modded_string
                    end
                else
                    key.each do |v|
                        expanded_receiveditem_methods[v] = value
                    end
                end
            else
                expanded_receiveditem_methods[key] = value
            end
        end

        return expanded_receiveditem_methods
    end
#--------------------------------------------------------------------------
# * Expand method hashes into new hashes
#--------------------------------------------------------------------------
    $expanded_progressive_methods = expand_progressive_methods(progressive_methods)
    $expanded_receiveditem_methods = expand_receiveditem_methods(receiveditem_methods)
#--------------------------------------------------------------------------
# * Method: Eval progressive methods
#--------------------------------------------------------------------------
    $progressive_counts = {}
    def progressive(key)
        if $expanded_progressive_methods.include?(key)
            $progressive_counts[key] = 0 unless $progressive_counts.include?(key)
            eval_target = $expanded_progressive_methods[key].fetch($progressive_counts[key], "puts \"[Archipelago_RGSS3] No defined method for index #{$progressive_counts[key]} in key #{key} in progressive_methods!\"")
            eval(eval_target)
            $progressive_counts[key] += 1
        else
            puts "[Archipelago_RGSS3] Key \"#{key}\" not found in progressive_methods!"
        end
    end
#--------------------------------------------------------------------------
# * Method: Use Text Input for details
#--------------------------------------------------------------------------
    def text_input(prompt)
        Input.update
        Graphics.update

        # A buffer to store the text in
        text = ""

        # Turn on text input
        Input.text_input = true

        # Wait until Enter gets pressed
        until Input.triggerex?(:RETURN)

            # Check for Ctrl+C and Ctrl+V!
            if Input.pressex?(:LCTRL) || Input.pressex?(:RCTRL)
                Input.clipboard = text if Input.triggerex?(:C)
                # << is faster than +=
                text << Input.clipboard if Input.triggerex?(:V)
            elsif Input.triggerex?(:BACKSPACE) or Input.timeex?(:BACKSPACE) >= 0.75
                text = text.chop
            else
                text << Input.gets
            end

            # Next frame
            Input.update
            Graphics.update
            $stdout.clear_screen
            puts "#{prompt} #{text}"
        end
        Input.text_input = false
        $stdout.clear_screen
        return text
    end
#--------------------------------------------------------------------------
# * Method: Use Keyboard Input to get connect details
#--------------------------------------------------------------------------
    def get_connect_details
        hostname = text_input("Hostname (will default to archipelago.gg if left blank):")
        port = text_input("Port:")
        name = text_input("Seat name:")
        password = text_input("Password (can be blank):")

        $archipelago.connect_info["hostname"] = hostname.empty? ? "archipelago.gg" : hostname
        $archipelago.connect_info["port"] = port.to_i
        $archipelago.connect_info["name"] = name
        $archipelago.connect_info["password"] = password unless password.empty?
    end
#--------------------------------------------------------------------------
# * Create a new TextInput Scene
#--------------------------------------------------------------------------
    class Scene_APConnectInput < Scene_Base
        def start
            super
            draw_image
        end
        def post_start
            super
            begin_text_input
            return_scene
        end
        def draw_image
            @pic = Sprite.new
            @pic.bitmap=Cache.custom("Pictures/text_input")
        end
        def begin_text_input
            get_connect_details
            $archipelago.connect
        end
        def update
            super
        end
    end
#--------------------------------------------------------------------------
# * Add get_connect method to Archipelago module
#--------------------------------------------------------------------------
    module Archipelago
        class Client
            def get_connect
                SceneManager.call(Scene_APConnectInput) unless @client_connect_status == Archipelago::ConnectStatus::CONNECTED
            end
        end
    end
#--------------------------------------------------------------------------
# * Initialize Archipelago Client
#--------------------------------------------------------------------------
    $archipelago = Archipelago::Client.new
    $archipelago.connect_info = {
        "game" => $archipelago_gamename,
        "items_handling" => $archipelago_items_handling
    }
#--------------------------------------------------------------------------
# * Override Cache to load Custom icons
#--------------------------------------------------------------------------
    module Cache
        def self.custom(filename)
            load_bitmap("Custom/Graphics/", filename)
        end
    end
#--------------------------------------------------------------------------
# * Override DataManager save/load methods
#--------------------------------------------------------------------------
    module DataManager
        def self.make_save_contents
            contents = {}
            contents[:system]        = $game_system
            contents[:timer]         = $game_timer
            contents[:message]       = $game_message
            contents[:switches]      = $game_switches
            contents[:variables]     = $game_variables
            contents[:self_switches] = $game_self_switches
            contents[:actors]        = $game_actors
            contents[:party]         = $game_party
            contents[:troop]         = $game_troop
            contents[:map]           = $game_map
            contents[:player]        = $game_player
            contents[:AP_connect_info] = $archipelago.connect_info if $load_autoconnect
            contents[:AP_receiveditems_index] = $receiveditems_index
            contents[:AP_progressive_counts] = $progressive_counts
            contents
        end

        def self.extract_save_contents(contents)
            $game_system        = contents[:system]
            $game_timer         = contents[:timer]
            $game_message       = contents[:message]
            $game_switches      = contents[:switches]
            $game_variables     = contents[:variables]
            $game_self_switches = contents[:self_switches]
            $game_actors        = contents[:actors]
            $game_party         = contents[:party]
            $game_troop         = contents[:troop]
            $game_map           = contents[:map]
            $game_player        = contents[:player]
            $archipelago.connect_info = contents[:AP_connect_info] if $load_autoconnect
            $receiveditems_index = contents[:AP_receiveditems_index]
            $progressive_counts = contents[:AP_progressive_counts]
        end

        def self.load_game(index)
            load_game_without_rescue(index)
            $archipelago.connect if $load_autoconnect
        rescue
            false
        end
    end
#--------------------------------------------------------------------------
# * Override Scene_Title.start to kill Archipelago connection
#--------------------------------------------------------------------------
    class Scene_Title < Scene_Base
        def start
            $archipelago.disconnect
            $archipelago = Archipelago::Client.new
            $archipelago.connect_info = {
                "game" => $archipelago_gamename,
                "items_handling" => $archipelago_items_handling
            }
            super
            SceneManager.clear
            Graphics.freeze
            create_background
            create_foreground
            create_command_window
            play_title_music
        end
    end
#--------------------------------------------------------------------------
# * On Connected: Begin ItemHandling thread
#--------------------------------------------------------------------------

    # This is extremely bad and I wish I did not have to do this
    unhandled_items = Queue.new
    $archipelago.add_listener("Connected") do |msg|
        Thread.new do
            loop do
                item = unhandled_items.pop(true) rescue nil
                if item
                    eval_target = $expanded_receiveditem_methods.fetch(item, "puts \"[Archipelago_RGSS3] No defined method for ReceivedItem ID #{item}!\"")
                    eval(eval_target)
                else
                    sleep 0.1
                end
                break if $archipelago.client_connect_status == Archipelago::ConnectStatus::DISCONNECTED
            end
        end
    end

#--------------------------------------------------------------------------
# * On ReceivedItems: Process Index, push item to handler
#--------------------------------------------------------------------------

    $receiveditems_index = 0
    $archipelago.add_listener("ReceivedItems") do |msg|
        item_counter = msg["index"]

        msg["items"].each do |item|
            if $receiveditems_index <= item_counter
                unhandled_items.push(item["item"])
                $receiveditems_index += 1
            end
            item_counter += 1
        end
    end

    # For future me, here's the old code but commented out
    #$receiveditems_index = 0
    #$archipelago.add_listener("ReceivedItems") do |msg|
    #    item_counter = msg["index"]
    #
    #    msg["items"].each do |item|
    #        if $receiveditems_index == item_counter
    #            eval_target = $expanded_receiveditem_methods.fetch(item, "puts \"[Archipelago_RGSS3] No defined method for ReceivedItem ID #{item}!\"")
    #            eval(eval_target)
    #            $receiveditems_index += 1
    #        end
    #        item_counter += 1
    #    end
    #end



