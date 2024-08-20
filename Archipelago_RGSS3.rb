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
    756783000 => "$game_party.add_actor(2)",  # Cupcake
    756783001 => "$game_party.add_actor(3)",  # Plush Foxy
    756783002 => "$game_party.add_actor(4)",  # Turret
    756783003 => "$game_party.add_actor(5)",  # Zombie
    756783004 => "$game_party.add_actor(6)",  # Pająk
    756783005 => "$game_party.add_actor(7)",  # Chlebek
    756783006 => "$game_party.add_actor(8)",  # Galaretka
    756783007 => "$game_party.add_actor(9)",  # Hater
    756783008 => "$game_party.add_actor(10)", # Dip
    756783009 => "$game_party.add_actor(11)", # Bob's Brain
    756783010 => "$game_party.add_actor(12)", # Bóbr
    756783011 => "$game_party.add_actor(13)", # Mroklum
    756783012 => "$game_party.add_actor(14)", # Robopirat
    756783013 => "$game_party.add_actor(15)", # Worms
    756783014 => "$game_party.add_actor(16)", # Slender
    756783015 => "$game_party.add_actor(17)", # Dingle
    756783016 => "$game_party.add_actor(18)", # Chica
    756783017 => "$game_party.add_actor(19)", # SCP-173
    756783018 => "$game_party.add_actor(20)", # Blue Baby
    756783019 => "$game_party.add_actor(21)", # Alex
    756783020 => "$game_party.add_actor(22)", # Robopirat Ninja
    756783021 => "$game_party.add_actor(23)", # Andre
    756783022 => "$game_party.add_actor(24)", # Globox
    756783023 => "$game_party.add_actor(25)", # Android
    756783024 => "$game_party.add_actor(26)", # Specimen 2
    756783025 => "$game_party.add_actor(27)", # Baloon Boy
    756783026 => "$game_party.add_actor(28)", # Toy Bonnie
    756783027 => "$game_party.add_actor(29)", # Rayman
    756783028 => "$game_party.add_actor(30)", # Kao
    756783029 => "$game_party.add_actor(31)", # Boogeyman
    756783030 => "$game_party.add_actor(32)", # Spooky
    756783031 => "$game_party.add_actor(33)", # Freddy
    756783032 => "$game_party.add_actor(34)", # Złoty Freddy
    756783033 => "$game_party.add_actor(35)", # Phantom Foxy
    756783034 => "$game_party.add_actor(36)", # SCP-049
    756783035 => "$game_party.add_actor(37)", # Reflux
    756783036 => "$game_party.add_actor(38)", # Jeff
    756783037 => "$game_party.add_actor(39)", # Isaac
    756783038 => "$game_party.add_actor(40)", # Azazel
    756783039 => "$game_party.add_actor(41)", # Monstro II
    756783040 => "$game_party.add_actor(42)", # Brzytwobrody
    756783041 => "$game_party.add_actor(43)", # Fuckboy
    756783042 => "$game_party.add_actor(44)", # Purple Guy
    756783043 => "$game_party.add_actor(45)", # BB
    756783044 => "$game_party.add_actor(46)", # SCP-106
    756783045 => "$game_party.add_actor(47)", # Kukiełka
    756783046 => "$game_party.add_actor(48)", # Ultra Greed
    756783047 => "$game_party.add_actor(49)", # Anim
    756783048 => "$game_party.add_actor(50)", # Cat Mario
    756783049 => "$game_party.add_actor(51)", # Indiana
    756783050 => "$game_party.add_actor(52)", # Serek(Kapłan)
    756783051 => "$game_party.add_actor(53)", # Lara Croft
    756783052 => "$game_party.add_actor(54)", # Serek(Wsparcie)
    756783053 => "$game_party.add_actor(55)", # Kaktus mag
    756783054 => "$game_party.add_actor(58)", # Papyrus

    # Key Items
    756783055 => "$game_party.gain_item($data_items[1], 1)",  # Kontroler
    756783056 => "$game_party.gain_item($data_items[2], 1)",  # Telefon
    756783057 => "$game_party.gain_item($data_items[3], 1)",  # Siekiera
    756783058 => "$game_party.gain_item($data_items[18], 1)", # Młotek
    756783059 => "$game_party.gain_item($data_items[21], 1)", # Karta klucz I
    756783060 => "$game_party.gain_item($data_items[22], 1)", # Karta klucz II
    756783061 => "$game_party.gain_item($data_items[23], 1)", # Karta klucz V
    756783062 => "$game_party.gain_item($data_items[46], 1)", # Przenośny teleport
    756783063 => "$game_party.gain_item($data_items[55], 1)", # Kartka papieru
    756783064 => "$game_party.gain_item($data_items[58], 1)", # Tajemnicza część
    756783065 => "$game_party.gain_item($data_items[62], 1)", # Buty Laury
    756783066 => "$game_party.gain_item($data_items[68], 1)", # Dysk do rzucania
    756783067 => "$game_party.gain_item($data_items[70], 1)", # Złoty klucz
    756783068 => "$game_party.gain_item($data_items[72], 1)", # Guziczek
    756783069 => "$game_party.gain_item($data_items[73], 1)", # Ołówek i gumka
    756783070 => "$game_party.gain_item($data_items[74], 1)", # Antygrawitacyjne buty
    756783071 => "$game_party.gain_item($data_items[16], 1)", # Klucz
    756783072 => "$game_party.gain_item($data_items[56], 1)", # Doggo


    #756783071 => "$game_party.gain_item($data_items[100], 1)", # Diamentowy pierścionek
    #756783071 => "$game_party.gain_item($data_items[10], 1)", # Krótkofalówka(Always)
    #756783071 => "$game_party.gain_item($data_items[11], 1)", # Krótkofalówka(Only in battle)
    #756783071 => "$game_party.gain_item($data_items[17], 5)", # Diament

    # Quest Items
    756783072 => "$game_party.gain_item($data_items[4], 5)",  # Złoty grzyb
    756783073 => "$game_party.gain_item($data_items[20], 1)", # Sos grzybowy

    # Fillers
    756783074 => "$game_party.gain_item($data_items[5], 15)",  # Jabłko
    756783075 => "$game_party.gain_item($data_items[6], 15)",  # Winoogrono
    756783076 => "$game_party.gain_item($data_items[7], 15)",  # Mandarynka
    756783077 => "$game_party.gain_item($data_items[8], 15)",  # Wiśnie
    756783078 => "$game_party.gain_item($data_items[9], 15)",  # Zioła
    756783079 => "$game_party.gain_item($data_items[12], 10)", # Czerwony lum
    756783080 => "$game_party.gain_item($data_items[13], 10)", # Niebieski lum
    756783081 => "$game_party.gain_item($data_items[14], 10)", # Żółty lum
    756783082 => "$game_party.gain_item($data_items[15], 15)", # Marchewka
    756783083 => "$game_party.gain_item($data_items[24], 1)",  # Srebrny klucz
    756783084 => "$game_party.gain_item($data_items[25], 15)", # Pomidor
    756783085 => "$game_party.gain_item($data_items[26], 15)", # Koniczyna
    756783086 => "$game_party.gain_item($data_items[27], 15)" # Pikantna papryka
    #TODO
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
# * Initialize Archipelago Client
#--------------------------------------------------------------------------
$archipelago = Archipelago::Client.new
$archipelago.connect_info = {
    "hostname" => CFG["Archipelago_Hostname"],
    "port" => CFG["Archipelago_Port"].to_i,
    "game" => $archipelago_gamename,
    "name" => CFG["Archipelago_Name"],
    "items_handling" => $archipelago_items_handling
}
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
        if $receiveditems_index < item_counter
            unhandled_items.push(item["item"])
            $receiveditems_index += 1
        elsif $receiveditems_index == item_counter
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



