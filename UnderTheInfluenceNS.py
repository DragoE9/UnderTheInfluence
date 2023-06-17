#imports
import nationstates
import math

#API setup stuff
user = input("Enter User Name: ")
api = nationstates.Nationstates(user + " Running UnderTheInfluenceNS.py by DragoE")
targ_region = input("Enter Target Region: ").lower().strip()
targ_region = targ_region.replace(" ","_")
api_region = api.region(targ_region)
inf_shard = nationstates.Shard("census", scale="65")

#define the extrapolation functions
def ExtrapolateEndos(targ_inf, start_inf, updates):
    endos = math.ceil((targ_inf - start_inf)/updates)
    return endos

def ExtrapolateTime(targ_inf, start_inf, endos):
    updates = math.ceil((targ_inf - start_inf)/(endos + 1))
    return updates


#Calculation shit
while True:
    user_input = input("Do you currently hold the delegacy? ").lower().strip()
    if user_input == "yes":
        #establish target values
        WAnations = int((api_region.get_shards("numwanations"))["numunnations"])
        total_nations = int(api_region.numnations)
        NoWA_nations = total_nations - WAnations
        if total_nations > 20:
            pass_cost = 20*total_nations
        else:
            pass_cost = 20*20
        secret_pass_cost = pass_cost * 2
        if NoWA_nations > 200:
            trans_cost = 20*200 + 80*WAnations
        else: 
            trans_cost = 20*NoWA_nations + 80*WAnations
        if trans_cost < 500:
            trans_cost = 500
        if (api_region.get_shards("frontier"))["frontier"] == 0:
            trans_cost = trans_cost*2
        #create a projection of raider deleg influence
        delegate = api_region.delegate
        api_nation = api.nation(delegate)
        del_endos = (api_nation.endorsements).split(",")
        num_endos = len(del_endos)
        influence = float((api_nation.get_shards(inf_shard))["census"]["scale"]["score"])
        #project time
        print("\n")
        pass_time = ExtrapolateTime(pass_cost,influence,num_endos)
        print("Visible password in {} updates ({} influence)".format(pass_time, pass_cost))
        secret_pass_time = ExtrapolateTime(secret_pass_cost,influence,num_endos)
        print("Secret password in {} updates ({} influence)".format(secret_pass_time, secret_pass_cost))
        transition_time = ExtrapolateTime(trans_cost,influence,num_endos)
        print("Governorship Seizable in {} updates ({} influence)".format(transition_time, trans_cost))
        #Extrapolation Section
        user_input = input("Would you like to extrapolate these results? ").lower().strip()
        if user_input == "yes":
            user_input = input("What are we extrapolating (visible/secret/governor)? ").lower().strip()
            user_time = int(input("In how many updates? "))
            if user_input == "visible":
                Endos = ExtrapolateEndos(pass_cost, influence, user_time)
                print("It would take {} endos to acheive that".format(Endos))
            elif user_input == "secret":
                Endos = ExtrapolateEndos(secret_pass_cost, influence, user_time)
                print("It would take {} endos to acheive that".format(Endos))
            elif user_input == "governor":
                Endos = ExtrapolateEndos(trans_cost, influence, user_time)
                print("It would take {} endos to acheive that".format(Endos))
        #end program
        break
    elif user_input == "no":
        #Account for sleeper inf
        sleeper_nation = input('Specify sleeper (enter "none" if not applicable): ').lower().strip()
        if sleeper_nation == "none":
            influence = 0
        else:
            sleeper_nation = sleeper_nation.replace(" ","_")
            api_nation = api.nation(sleeper_nation)
            influence = float((api_nation.get_shards(inf_shard))["census"]["scale"]["score"])
        #establish target values
        WAnations = int((api_region.get_shards("numwanations"))["numunnations"])
        total_nations = int(api_region.numnations)
        NoWA_nations = total_nations - WAnations
        if total_nations > 20:
            pass_cost = 20*total_nations
        else:
            pass_cost = 20*20
        secret_pass_cost = pass_cost * 2
        if NoWA_nations > 200:
            trans_cost = 20*200 + 80*WAnations
        else: 
            trans_cost = 20*NoWA_nations + 80*WAnations
        if trans_cost < 500:
            trans_cost = 500
        if (api_region.get_shards("frontier"))["frontier"] == 0:
            trans_cost = trans_cost*2
        #Mode Selection
        user_input = input("Select Fixed Time Mode or Fixed Endos Mode (time/endo): ").lower().strip()
        if user_input == "time":
            updates = int(input("Choose desired number of updates: "))
            print("\n")
            #Calc Endos Required
            visible_endos = ExtrapolateEndos(pass_cost,influence,updates)
            print("It would take {} endos to get a Visible Password ({} influence)".format(visible_endos,pass_cost))
            secret_endos = ExtrapolateEndos(secret_pass_cost,influence,updates)
            print("It would take {} endos to get a Secret Password ({} influence)".format(secret_endos,secret_pass_cost))
            trans_endos = ExtrapolateEndos(trans_cost,influence,updates)
            print("It would take {} endos to Seize the Governorship ({} influence)".format(trans_endos,trans_cost))
        elif user_input == "endo":
            endos = int(input("How many endos will you have? "))
            print("\n")
            #Calc Time Required
            visible_time = ExtrapolateTime(pass_cost,influence,endos)
            print("It would take {} updates to get a Visible Password ({} influence)".format(visible_time,pass_cost))
            secret_time = ExtrapolateTime(secret_pass_cost,influence,endos)
            print("It would take {} updates to get a Secret Password ({} influence)".format(secret_time,secret_pass_cost))
            trans_time = ExtrapolateTime(trans_cost,influence,endos)
            print("It would take {} updates to Seize the Governorship ({} influence)".format(trans_time,trans_cost))
        #end program
        break
    else:
        print("Error, unrecognized response")
