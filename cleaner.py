def clean_chat(chat):
    # Declarations
    chat = chat.lower()
    messages = []
    final_str = ""

    # Cleaning
    for char in chat:
        messages.append(char)
        if ord(char) == 10:  # Check for newline character
            message = "".join(messages)
            if (
                "<media omitted>" not in message
                and "https" not in message
                and ":" in message
            ):
                final_str += message[18:]
            messages = []  # In any case, clear the messages

    # Output
    return final_str


def save_to_file(output, output_path):
    with open(output_path, "w") as file:
        file.write(output)


# Example usage:
original_chat = """
6/27/23, 10:12 - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.
10/16/22, 07:40 - MrPatrick created group "Sisi Village ground team"
6/27/23, 10:12 - Phil added you
6/27/23, 10:14 - Phil added +254 707 549708
6/27/23, 20:54 - +254 707 549708: This message was deleted
6/28/23, 20:52 - +254 113536420: Ogalo we continue with bedding
6/28/23, 20:52 - +254 113536420: These is our seedlings in Ogallo Nursery, now it's one week old.
6/28/23, 20:52 - +254 113536420: <Media omitted>
6/28/23, 20:52 - +254 113536420: <Media omitted>
6/28/23, 20:52 - +254 113536420: <Media omitted>
6/28/23, 20:52 - +254 113536420: <Media omitted>
6/28/23, 20:52 - +254 113536420: <Media omitted>
6/29/23, 04:42 - MrPatrick: Effort looking great!!!
6/29/23, 20:16 - +254 113536420: This message was deleted
6/29/23, 20:17 - +254 113536420: <Media omitted>
6/29/23, 20:17 - +254 113536420: <Media omitted>
6/29/23, 20:17 - +254 113536420: <Media omitted>
6/29/23, 20:22 - +254 113536420: We're now almost to go through with Phase One A of 3 Blocks
6/29/23, 20:47 - MrPatrick: That is great
6/30/23, 10:32 - +254 100323790: <Media omitted>
6/30/23, 11:15 - MrPatrick: 👏👏👏
6/30/23, 11:45 - +254 722 496898: 👏👏👏
6/30/23, 12:18 - +254 724 850009: <Media omitted>
6/30/23, 12:19 - +254 722 496898: 👍
6/30/23, 12:42 - +254 714 783208: <Media omitted>
6/30/23, 13:00 - +254 714 783208: <Media omitted>
6/30/23, 13:00 - +254 714 783208: <Media omitted>
6/30/23, 13:03 - +254 710 364257: <Media omitted>
6/30/23, 13:28 - +254 710 338421: <Media omitted>
6/30/23, 13:29 - +254 710 338421: <Media omitted>
6/30/23, 13:31 - +254 710 338421: <Media omitted>
6/30/23, 17:59 - +254 113536420: We are still moving
6/30/23, 18:20 - +254 113536420: <Media omitted>
6/30/23, 18:20 - +254 113536420: <Media omitted>
6/30/23, 18:20 - +254 113536420: <Media omitted>
7/1/23, 06:56 - +254 724 957698: Austin, Ambassadors post on ambassadors wall. But I appreciate your point in regard to blanket adoption of modern farm inputs.
7/1/23, 07:31 - +254 721 337221: <Media omitted>
7/1/23, 07:31 - +254 721 337221: <Media omitted>
7/1/23, 07:31 - +254 721 337221: <Media omitted>
7/1/23, 07:31 - +254 721 337221: <Media omitted>
7/1/23, 07:33 - +254 721 337221: <Media omitted>
7/1/23, 07:33 - +254 721 337221: <Media omitted>
7/1/23, 07:35 - +254 721 337221: <Media omitted>
7/1/23, 07:36 - +254 721 337221: <Media omitted>
7/1/23, 07:36 - +254 721 337221: <Media omitted>
7/1/23, 07:36 - +254 721 337221: <Media omitted>
7/1/23, 08:01 - +254 721 337221: <Media omitted>
7/1/23, 08:01 - +254 721 337221: Likuyani demo farm replacement
7/1/23, 08:01 - +254 721 337221: <Media omitted>
7/1/23, 08:14 - +254 710 338421: Can we think of partial/comprehensive sterilization of nursery soils at mixing stage? It is apparent that there are soil born pests and diseases.
7/1/23, 08:16 - +254 710 338421: https://nation.africa/kenya/news/new-tough-bill-criminalises-use-of-animal-manure-152364
7/1/23, 08:16 - +254 710 338421: If a farmer can't use animal manure and can't access/safely use inorganic fertilizers continuously, then what next? Do we stop crop production altogether?
7/1/23, 08:33 - MrPatrick: Painful but must be done!!! We keep standards at Sisi. The seedlings were fine but lacked water.
7/1/23, 08:36 - +254 721 337221: <Media omitted>
7/1/23, 08:36 - +254 721 337221: <Media omitted>
7/1/23, 08:36 - +254 721 337221: <Media omitted>
7/1/23, 08:38 - +254 721 337221: Now in Likuyani we have 414 trees. Out that we are replacing 160 seedlings that did not pick well because of the hard conditions or missing water .
7/1/23, 08:40 - +254 721 337221: <Media omitted>
7/1/23, 08:40 - +254 721 337221: <Media omitted>
7/1/23, 08:41 - +254 721 337221: <Media omitted>
7/1/23, 08:43 - MrPatrick: Painful Sisi standard. Yet we must !!!
7/1/23, 09:01 - +254 721 337221: <Media omitted>
7/1/23, 09:06 - +254 724 957698: That clip you are showing with dead roots is indicative 2 possible problems
1. Poor planting material and knotted roots when planting.
2. Presence of nematodes. Nematodes are serlous pests here and I've had to use appropriate measures  to control them. The demo farm has not received this treatment
7/1/23, 09:14 - +254 710 338421: Soil dressing with nematicide?
7/1/23, 09:29 - MrPatrick: We are ready to collect huge volumes of mature Hass avocado fruits. Get in touch with me
7/1/23, 12:19 - +254 100323790: It might have been poor soil mixing.
7/1/23, 12:39 - +254 721 337221: <Media omitted>
7/1/23, 12:39 - +254 721 337221: <Media omitted>
7/1/23, 12:42 - +254 721 337221: <Media omitted>
7/1/23, 12:42 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 12:48 - +254 721 337221: <Media omitted>
7/1/23, 13:01 - +254 742 254722: Waiting for this message
7/1/23, 13:01 - +254 742 254722: Waiting for this message
7/1/23, 13:01 - +254 742 254722: Waiting for this message
7/1/23, 13:04 - +254 721 337221: <Media omitted>
7/1/23, 13:04 - +254 721 337221: <Media omitted>
7/1/23, 13:19 - +254 721 337221: Malava team kindly coming for us to go to malangas farm
7/1/23, 13:25 - +254 721 337221: <Media omitted>
7/1/23, 13:25 - +254 721 337221: <Media omitted>
7/1/23, 13:25 - +254 721 337221: <Media omitted>
7/1/23, 13:25 - +254 721 337221: <Media omitted>
7/1/23, 13:25 - +254 721 337221: <Media omitted>
7/1/23, 13:27 - +254 721 337221: <Media omitted>
7/1/23, 13:27 - +254 721 337221: <Media omitted>
7/1/23, 13:27 - +254 721 337221: <Media omitted>
7/1/23, 13:27 - +254 721 337221: <Media omitted>
7/1/23, 13:27 - +254 721 337221: <Media omitted>
7/1/23, 14:35 - MrPatrick: Is this Kimilili?
7/1/23, 14:36 - MrPatrick: Keep it up the good work Japheth
7/1/23, 14:46 - +254 721 337221: <Media omitted>
7/1/23, 14:46 - +254 721 337221: <Media omitted>
7/1/23, 14:46 - +254 721 337221: <Media omitted>
7/1/23, 14:46 - +254 721 337221: <Media omitted>
7/1/23, 14:46 - +254 721 337221: <Media omitted>
7/1/23, 14:47 - +254 721 337221: <Media omitted>
7/1/23, 14:47 - +254 721 337221: <Media omitted>
7/1/23, 14:47 - +254 721 337221: <Media omitted>
7/1/23, 14:47 - +254 721 337221: <Media omitted>
7/1/23, 14:49 - +254 721 337221: <Media omitted>
7/1/23, 21:48 - +254 710 338421: What is the intercrop?
7/1/23, 21:57 - MrPatrick: Linci you may answer this
7/1/23, 22:35 - +254 721 337221: Intercropping is ....
You have your avocado as the main crop and target crop, but then because you have the interval of 6m from bed to bed, you decide not to leave the space empty, so you can maintain the interroads by planting short crops that will not grow and give a shadow to the trees.
7/1/23, 22:49 - MrPatrick: What crop was it in the photo
7/1/23, 22:55 - +254 721 337221: Groundnuts in lugulu
Mitoo in Kimilili
Spring onion in Likuyani
7/2/23, 07:31 - MrPatrick: Our Quality Assurance Officer will guide us
7/2/23, 08:17 - +254 721 337221: <Media omitted>
7/2/23, 08:17 - +254 721 337221: <Media omitted>
7/2/23, 08:17 - +254 721 337221: <Media omitted>
7/2/23, 08:17 - +254 721 337221: <Media omitted>
7/2/23, 08:17 - +254 721 337221: <Media omitted>
7/2/23, 08:20 - +254 721 337221: <Media omitted>
7/2/23, 08:20 - +254 721 337221: <Media omitted>
7/2/23, 08:20 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:49 - +254 721 337221: <Media omitted>
7/2/23, 09:50 - +254 721 337221: Ogallo orchards
7/2/23, 10:10 - +254 721 337221: All,
From next week kindly send your wages by Friday to Sam. You can include Saturday's .
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/2/23, 16:59 - +254 721 337221: <Media omitted>
7/3/23, 11:09 - +254 790 433944: <Media omitted>
7/3/23, 11:10 - +254 790 433944: <Media omitted>
7/3/23, 11:10 - +254 790 433944: <Media omitted>
7/3/23, 11:10 - +254 790 433944: <Media omitted>
7/3/23, 11:11 - +254 790 433944: <Media omitted>
7/3/23, 11:11 - +254 790 433944: <Media omitted>
7/3/23, 13:04 - MrPatrick: This is great
7/3/23, 15:34 - +254 113536420: <Media omitted>
7/3/23, 15:34 - +254 113536420: <Media omitted>
7/3/23, 15:34 - +254 113536420: <Media omitted>
7/3/23, 15:34 - +254 113536420: <Media omitted>
7/3/23, 15:35 - +254 113536420: Ogalo bedding is going on
7/3/23, 16:02 - MrPatrick: Keep it up
7/4/23, 11:42 - +254 113536420: <Media omitted>
7/4/23, 11:43 - +254 113536420: <Media omitted>
7/4/23, 11:43 - +254 113536420: <Media omitted>
7/4/23, 11:43 - +254 113536420: <Media omitted>
7/4/23, 11:43 - +254 113536420: <Media omitted>
7/4/23, 11:44 - +254 113536420: <Media omitted>
7/4/23, 11:45 - +254 113536420: <Media omitted>
7/4/23, 11:45 - +254 113536420: <Media omitted>
7/4/23, 11:45 - +254 113536420: <Media omitted>
7/4/23, 11:46 - +254 113536420: Ogalo we started fencing while in the other side bedding is in progress on Phase One B blocks
7/4/23, 11:48 - MrPatrick: That is great!!!
7/4/23, 11:51 - +254 113536420: <Media omitted>
7/4/23, 11:57 - +254 721 337221: Very important
7/4/23, 11:57 - +254 721 337221: We need to plant in 2 weeks time
7/4/23, 12:02 - +254 113536420: <Media omitted>
7/4/23, 12:02 - +254 113536420: <Media omitted>
7/4/23, 14:11 - +254 742 254722: <Media omitted>
7/4/23, 14:11 - +254 742 254722: <Media omitted>
7/4/23, 14:21 - +254 742 254722: <Media omitted>
7/4/23, 15:58 - MrPatrick: <Media omitted>
7/4/23, 15:59 - MrPatrick: Ogalo on track
7/4/23, 16:00 - +254 721 337221: Great team
7/4/23, 16:01 - MrPatrick: Great work Haron
7/4/23, 16:15 - +254 721 337221: Good evening all,
This is to bring to your attention that no seedlings will be replaced without a report on why we are replacing and the cause.
The field officers should be able to observe the dead seedlings and see the possible causes of dead plants then make a report that will be used to determine whether it's our seedlings quality or a problem caused by the farmer himself.
Then we will decide if he buys again the replacement seedlings or we carry the cost.
Kindly I hope am clear if not understood please call.
Rgds,
Linci sm
7/4/23, 16:18 - +254 721 337221: Faith,
You are tasked to look at the dead seedlings before replacement as the Quality assurance manager and help on the decision of replacement
7/4/23, 16:24 - +254 714 783208: Noted
7/4/23, 18:04 - +254 790 433944: Oky sawa 🙏
7/4/23, 18:05 - +254 790 433944: <Media omitted>
7/4/23, 18:05 - +254 790 433944: <Media omitted>
7/4/23, 18:05 - +254 790 433944: <Media omitted>
7/4/23, 18:07 - +254 790 433944: <Media omitted>
7/4/23, 18:11 - MrPatrick: Good job Timo
7/5/23, 18:05 - +254 113536420: Ogalo we continue with bedding and fencing
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 18:05 - +254 113536420: <Media omitted>
7/5/23, 20:36 - +254 790 433944: <Media omitted>
7/5/23, 20:36 - +254 790 433944: <Media omitted>
7/5/23, 20:36 - +254 790 433944: <Media omitted>
7/5/23, 20:36 - +254 790 433944: <Media omitted>
7/5/23, 20:37 - +254 790 433944: <Media omitted>
7/5/23, 20:39 - +254 790 433944: <Media omitted>
7/5/23, 20:39 - +254 790 433944: <Media omitted>
7/5/23, 20:40 - +254 790 433944: <Media omitted>
7/6/23, 11:41 - +254 724 850009: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 14:52 - +254 790 148692: <Media omitted>
7/6/23, 15:41 - +254 790 433944: <Media omitted>
7/6/23, 15:41 - +254 790 433944: <Media omitted>
7/6/23, 15:41 - +254 790 433944: <Media omitted>
7/6/23, 15:42 - +254 790 433944: <Media omitted>
7/6/23, 15:42 - +254 790 433944: <Media omitted>
7/6/23, 15:43 - +254 790 433944: <Media omitted>
7/6/23, 16:00 - MrPatrick: This is great
7/6/23, 17:29 - +254 701 843384: Good
7/7/23, 13:02 - MrPatrick: <Media omitted>
7/7/23, 18:48 - +254 742 254722: <Media omitted>
7/7/23, 18:48 - +254 742 254722: <Media omitted>
7/7/23, 18:48 - +254 742 254722: <Media omitted>
7/7/23, 19:35 - MrPatrick: This is great!!
7/8/23, 12:55 - +254 710 338421: That's a great challenge for SISI to go all avocado!
7/8/23, 15:05 - +254 113536420: Fencing in progress at Ogallo demo farm.
7/8/23, 15:05 - +254 113536420: We are now almost to clear Phase One B blocks in the next 2 days coming, I hope it will be through on Tuesday next week.
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:06 - +254 113536420: <Media omitted>
7/8/23, 15:09 - +254 113536420: <Media omitted>
7/8/23, 16:34 - +254 790 148692: <Media omitted>
7/8/23, 16:34 - +254 790 148692: <Media omitted>
7/8/23, 16:35 - +254 790 148692: <Media omitted>
7/8/23, 16:35 - +254 790 148692: <Media omitted>
7/8/23, 16:36 - +254 790 148692: <Media omitted>
7/8/23, 16:36 - +254 790 148692: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 13:40 - MrPatrick: <Media omitted>
7/9/23, 15:16 - +254 722 709250: Building bridges for Sisi Village,I guess.
7/9/23, 15:36 - MrPatrick: You are right!!
7/9/23, 15:57 - +254 100323790: Wau the sky is the limit.
7/9/23, 16:11 - +254 100323790: <Media omitted>
7/9/23, 16:43 - MrPatrick: <Media omitted>
7/9/23, 21:45 - MrPatrick: <Media omitted>
7/9/23, 21:45 - MrPatrick: Cooperatives would settle this issue
7/10/23, 18:25 - +254 742 254722: <Media omitted>
7/10/23, 18:26 - +254 742 254722: <Media omitted>
7/10/23, 18:26 - +254 742 254722: <Media omitted>
7/10/23, 18:27 - MrPatrick: Where is this ?
7/10/23, 18:31 - +254 742 254722: <Media omitted>
7/10/23, 18:33 - +254 742 254722: Sirakaru area near Lwandet region
7/10/23, 18:46 - +254 113536420: This message was deleted
7/10/23, 19:00 - +254 113536420: <Media omitted>
7/10/23, 19:00 - +254 113536420: <Media omitted>
7/10/23, 19:00 - +254 113536420: <Media omitted>
7/10/23, 19:00 - +254 113536420: <Media omitted>
7/10/23, 19:00 - +254 113536420: <Media omitted>
7/10/23, 19:01 - +254 113536420: <Media omitted>
7/10/23, 19:01 - +254 113536420: <Media omitted>
7/10/23, 19:03 - +254 113536420: <Media omitted>
7/10/23, 19:03 - +254 113536420: <Media omitted>
7/10/23, 19:03 - +254 113536420: Ogalo fencing and bedding in progress
7/10/23, 19:27 - +254 113536420: Today we visited a farmer in Butula sub-account, Tingolo area Busia County, farmer interested to plant a Hass  Avocado in his farm of a half an acre. The soil is fine and there's a lot of spring water from the ground and he's willing to start with 1/4 an acre first
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:34 - +254 113536420: <Media omitted>
7/10/23, 19:35 - +254 113536420: <Media omitted>
7/10/23, 19:35 - +254 113536420: <Media omitted>
7/10/23, 19:35 - +254 113536420: <Media omitted>
7/11/23, 05:49 - MrPatrick: *❗3 MAJOR PROTESTS TO TAKE PLACE ON WEDNESDAY: ❗* 


■ Warnings are spreading out that Kenyans should prepare for major disruptions on Wednesday, July 12, as the nation anticipates three significant protests across different sectors. 

■ These demonstrations are likely to have a considerable impact on day-to-day operations with projected depth pitted to be bigger than the previous protests.

■ The occurrence of these simultaneous events can be attributed to the disillusionment felt by Kenyans regarding the soaring cost of living and contentious tax hikes.

■ The strike notices issued by various key stakeholders are also expected to paralyze the transport sector, forcing Kenyans to seek alternative means to head to work.


● Taxi association protests

■ Taxi-hailing apps announced a nationwide strike on Wednesday, July 12, over various issues ailing the transport sector. 

■ The leadership of the  taxi-hailing association highlighted several key concerns that they seek to address, which include; insecurity, escalating fuel prices, and pay rates set by digital companies.


■ A strict warning was also sent to all taxi-hailing drivers to keep their cars off the road during the strike. 

■ The leadership argued that the strike would continue until their demands are met by the government.

"Do not try to put your car on the road. We are warning you not to try to test the waters on the day of the strike," a source has intimated.

● PSV Protests

■ On June 21, 2023, Public Service Vehicles (PSVs) issued a 21-day strike notice over the mandatory re-testing exercise conducted by the National Transport and Safety Authority (NTSA).
 The deadline is set to lapse on Wednesday, July 12.

■ Supported by long-distance drivers and boda boda operators, the PSV operators argued that the mandatory re-testing was punitive and aimed at frustrating motorists.

■ They sought to be involved in the decision-making process in a bid to guarantee positive changes within the sector.

"The association calls for constructive dialogue between the Ministry of Transport, the NTSA, and stakeholders to address concerns and find mutually beneficial solutions that prioritise safety while supporting driver's well-being," read part of a statement by the Long-Distance Drivers and Conductors Association (LODDCA).

■ Azimio Protest

● During the Saba Saba demonstrations, Azimio la Umoja Raila Odinga announced nationwide protests that would continue his clarion call for civil disobedience. 
● He warned the Kenya Kwanza administration that issues such as punitive taxes and the high cost of living were non-negotiable.

"And come next week July 12 (Wednesday) we're going to have more serious demonstrations across the country," stated National Assembly Minority Leader Opiyo Wandayi.

"Today (on July 7) was the beginning of this new wave of civil disobedience and mass action," he added.

■ While making his remarks, the opposition leader rallied behind the push to collect 10 million signatures - a statement which drew criticism from the Kenya Kwanza leaders who argued that the signatures could not kick out President William Ruto from office and this is an attempt to overthrow government which will be met with the full wrath as intimated by Kenya Kwanza.

■ Wednesday is projected to be vicious especially after threats that Opposition leader could be arrested an issue thst could ignite abrassion along streets of the capital.

■ Plan your schedules accordingly .
7/11/23, 05:51 - MrPatrick: Let’s attend to Sisi work with caution
7/11/23, 06:48 - +254 721 337221: <Media omitted>
7/11/23, 06:48 - +254 721 337221: Green gold
7/11/23, 06:54 - MrPatrick: Yes it is!!
7/11/23, 07:58 - +254 790 148692: <Media omitted>
7/11/23, 07:58 - +254 790 148692: <Media omitted>
7/11/23, 07:58 - +254 790 148692: <Media omitted>
7/11/23, 07:59 - +254 790 148692: <Media omitted>
7/11/23, 07:59 - +254 790 148692: <Media omitted>
7/11/23, 08:02 - +254 790 148692: 11/07/2023
Kimilili
Grafting ongoing since last Saturday, also sorting of young seedlings Tobe grafted to be done today, grafting may end today.watering done because it is not raining
7/11/23, 08:02 - MrPatrick: 👏👏👏
7/11/23, 08:16 - MrPatrick: http://opr.news/s61e3ce76230711en_ke?link=1&client=iosnews
7/11/23, 08:49 - +254 100323790: <Media omitted>
7/11/23, 08:56 - +254 100323790: <Media omitted>
7/11/23, 15:51 - +254 113536420: This message was deleted
7/11/23, 17:38 - +254 719 852892: <Media omitted>
7/11/23, 17:38 - +254 719 852892: <Media omitted>
7/11/23, 23:02 - MrPatrick: 👏👏👏
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:08 - +254 790 148692: <Media omitted>
7/12/23, 00:09 - +254 790 148692: <Media omitted>
7/12/23, 17:04 - +254 113536420: Ogalo Phase One A and B blocks are now complete
7/12/23, 17:05 - +254 113536420: <Media omitted>
7/12/23, 17:05 - +254 113536420: <Media omitted>
7/12/23, 17:05 - +254 113536420: <Media omitted>
7/12/23, 17:06 - +254 113536420: <Media omitted>
7/12/23, 17:06 - +254 113536420: <Media omitted>
7/12/23, 17:07 - +254 113536420: <Media omitted>
7/12/23, 17:18 - +254 113536420: Is the  fencing materials in our Demo farm
7/12/23, 17:18 - +254 113536420: <Media omitted>
7/12/23, 17:18 - +254 113536420: <Media omitted>
7/12/23, 17:18 - +254 113536420: <Media omitted>
7/12/23, 17:42 - +254 113536420: Ogalo seedlings that came first day in right side are picking well and the left side are also starting to pick. Acclimatization of 21 days and 13 days
7/12/23, 17:42 - +254 113536420: <Media omitted>
7/12/23, 17:48 - +254 721 337221: This is good
7/12/23, 22:42 - MrPatrick: Great
7/12/23, 22:42 - MrPatrick: Great
7/13/23, 08:11 - +254 721 337221: https://www.linkedin.com/posts/paul-huish-3ba52558_careergrowth-employeegrowth-careerdevelopment-activity-7083727921000910848-99w6?utm_source=share&utm_medium=member_android
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 10:40 - +254 790 148692: <Media omitted>
7/13/23, 12:43 - MrPatrick: Great
7/13/23, 12:46 - +254 113536420: Ogalo construction of fencing is starting
7/13/23, 12:50 - MrPatrick: 👏👏👏
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 12:56 - +254 113536420: <Media omitted>
7/13/23, 17:52 - +254 719 852892: <Media omitted>
7/13/23, 17:54 - +254 790 148692: <Media omitted>
7/13/23, 18:09 - +254 721 337221: Excellent
7/13/23, 18:47 - +254 719 852892: <Media omitted>
7/13/23, 18:51 - +254 719 852892: <Media omitted>
7/13/23, 18:51 - +254 719 852892: <Media omitted>
7/13/23, 19:41 - +254 719 852892: <Media omitted>
7/13/23, 20:44 - MrPatrick: This is such good news
7/13/23, 21:26 - +254 790 148692: <Media omitted>
7/13/23, 23:08 - MrPatrick: We can’t go this route
7/14/23, 14:30 - +254 722 502957: <Media omitted>
7/14/23, 14:32 - +254 721 337221: Great Mugendi
7/14/23, 14:36 - +254 722 502957: <Media omitted>
7/14/23, 15:11 - +254 714 783208: <Media omitted>
7/14/23, 15:11 - +254 714 783208: <Media omitted>
7/14/23, 15:38 - MrPatrick: 👍🏽
7/14/23, 15:39 - MrPatrick: 👍🏽
7/14/23, 15:48 - +254 710 338421: What's happening on this farm?
7/14/23, 17:04 - MrPatrick: Which farm ambassador
7/14/23, 20:17 - +254 710 338421: Image by Mr. Siimiyu showing what appears to be a gully caused by erosion?
7/14/23, 20:46 - MrPatrick: It was pit prepared for planting avocado 😳😳
7/14/23, 20:47 - +254 721 337221: Our people don't have knowledge
7/14/23, 20:47 - +254 721 337221: Sisi village is there for that
7/14/23, 21:55 - +254 113536420: Ogalo team, we meet a group of 24 farmers in Mayoni Ward  who are interested to join us. they are willing to plant Hass 🥑 Avocado
7/14/23, 22:01 - +254 113536420: <Media omitted>
7/14/23, 22:02 - +254 113536420: <Media omitted>
7/14/23, 22:12 - +254 113536420: At Ogallo demo farm
7/14/23, 22:17 - +254 113536420: <Media omitted>
7/14/23, 22:17 - +254 113536420: <Media omitted>
7/14/23, 22:17 - +254 113536420: <Media omitted>
7/14/23, 22:17 - +254 113536420: <Media omitted>
7/14/23, 22:17 - +254 113536420: <Media omitted>
7/14/23, 22:18 - +254 113536420: <Media omitted>
7/15/23, 17:56 - +254 113536420: Ogalo fencing is still going on
7/15/23, 17:57 - +254 113536420: <Media omitted>
7/15/23, 17:57 - +254 113536420: <Media omitted>
7/15/23, 17:57 - +254 113536420: <Media omitted>
7/15/23, 17:57 - +254 113536420: <Media omitted>
7/16/23, 07:29 - MrPatrick: <Media omitted>
7/16/23, 07:32 - MrPatrick: <Media omitted>
7/17/23, 15:24 - +254 100323790: <Media omitted>
7/17/23, 15:45 - +254 721 337221: How is the wetness of that soil? Looks dry or moist
7/17/23, 15:47 - +254 100323790: The soil is moist
7/17/23, 15:52 - +254 721 337221: We need to learn about moisture content of the soil when planting
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:07 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:11 - +254 790 148692: <Media omitted>
7/17/23, 16:50 - +254 100323790: The soil is okay and water is readily available. There is a well and a river nearby.
7/17/23, 17:24 - +254 721 337221: Advice the farmer to make sure the tree gets water every day
7/17/23, 17:25 - +254 100323790: Noted
7/17/23, 17:36 - +254 113536420: Today we have received 29 bags of rootstock seeds in Ogallo
7/17/23, 17:36 - +254 113536420: <Media omitted>
7/17/23, 17:36 - +254 113536420: <Media omitted>
7/17/23, 17:36 - +254 113536420: <Media omitted>
7/17/23, 17:36 - +254 113536420: <Media omitted>
7/17/23, 17:41 - +254 113536420: Ogalo fencing is going on
7/17/23, 17:41 - +254 113536420: <Media omitted>
7/17/23, 17:45 - +254 113536420: <Media omitted>
7/17/23, 17:46 - +254 113536420: <Media omitted>
7/17/23, 18:10 - +254 113536420: <Media omitted>
7/17/23, 18:10 - +254 113536420: <Media omitted>
7/17/23, 20:23 - +254 719 852892: <Media omitted>
7/17/23, 20:49 - +254 719 852892: <Media omitted>
7/18/23, 11:17 - MrPatrick: <Media omitted>
7/18/23, 11:18 - MrPatrick: <Media omitted>
7/18/23, 11:49 - +254 721 337221: <Media omitted>
7/18/23, 11:49 - +254 721 337221: <Media omitted>
7/18/23, 11:49 - +254 721 337221: <Media omitted>
7/18/23, 11:49 - +254 721 337221: <Media omitted>
7/18/23, 11:50 - +254 721 337221: Simiyu great Job
7/18/23, 15:52 - +254 721 337221: <Media omitted>
7/18/23, 15:52 - +254 721 337221: <Media omitted>
7/18/23, 15:52 - +254 721 337221: <Media omitted>
7/18/23, 15:52 - +254 721 337221: <Media omitted>
7/18/23, 15:52 - +254 721 337221: <Media omitted>
7/18/23, 15:53 - +254 721 337221: Kaimosi team:
This is excellent and at 1yr 2 months, you are on the right path. Am seeing us give it time to do fast flowering in 2 yrs. This means next year may the flowering that will happen we leave it.
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:02 - +254 721 337221: <Media omitted>
7/18/23, 16:03 - +254 721 337221: Saleh,
This is a good response from those seedlings. 
Give them more 2 weeks and please water daily and you are ok to go with the best seedlings.
7/18/23, 16:04 - +254 721 337221: Malava:
Let's have your photos of the demo and the seedlings
Clear ones.
7/18/23, 16:05 - +254 721 337221: Ambassador Sarah:
Send us what's happening in Kimilili both demo and seeslings
7/18/23, 16:06 - +254 721 337221: Ambassador Kadima:
How are the trees that we replaced at the demo farm?
How are the old ones at the demo farm?
How are the seedlings?
7/18/23, 16:06 - +254 721 337221: Faith:
What is the state of the farms you have visited? Are we moving on well basing on age, quality and irrigation?
7/18/23, 16:14 - +254 714 783208: Good evening team
Most of the farms are doing okay.
The farms that were having issues with some of the seedlings got a replacement.
Some of the first farmers who planted avocado were struggling with their trees but after a couple of visits they are now seeing improvement
7/18/23, 16:20 - +254 721 337221: Great,
Can you also start advising on nutrition and fertigation as we need to start raising the trees on a right path than correcting later. 
Hygiene
Prunning
Fertigation
7/18/23, 16:20 - +254 721 337221: Irrigation
7/18/23, 16:24 - +254 714 783208: Sawa
7/18/23, 16:24 - +254 721 337221: It should reflect all your records as what you started at kaimosi.
When am there I need to see some files on Kaimosi farm, and all other farms we have started.
On the things mentioned:
Land preparation
Seedlings date of propagation
Date of planting and dimensions
Water/type of irrigation in place
How many times irrigation is done
Replacement dates if any
Reason for replacement
Prunning dates
Weeding dates
Fertilizer application dates
Any other activities
7/18/23, 16:26 - +254 721 337221: Ambassadors help on making sure the field guys are keeping records and anything happening everyday in the farms you are manning. 
Faith give then formats/ sheets to use.
7/18/23, 16:41 - +254 714 783208: Okay
7/18/23, 16:45 - +254 721 337221: Great
7/18/23, 16:46 - +254 721 337221: Also start developing a sheet that will have all problems you see on different farms for your quality checks, Different farms have different issues technically.
7/18/23, 18:23 - +254 719 852892: This is so interesting and  encouraging!
7/18/23, 20:00 - +254 113536420: Ogalo we wash seeds and the other side fencing on going
7/18/23, 20:00 - +254 113536420: <Media omitted>
7/18/23, 20:00 - +254 113536420: <Media omitted>
7/18/23, 20:00 - +254 113536420: <Media omitted>
7/18/23, 20:00 - +254 113536420: <Media omitted>
7/18/23, 20:00 - +254 113536420: <Media omitted>
7/18/23, 20:57 - +254 719 852892: <Media omitted>
7/18/23, 21:04 - +254 719 852892: <Media omitted>
7/19/23, 10:54 - +254 724 850009: <Media omitted>
7/19/23, 10:55 - +254 724 850009: <Media omitted>
7/19/23, 10:55 - +254 724 850009: <Media omitted>
7/19/23, 10:55 - +254 724 850009: <Media omitted>
7/19/23, 11:03 - +254 724 850009: <Media omitted>
7/19/23, 11:05 - +254 724 850009: <Media omitted>
7/19/23, 17:19 - +254 719 852892: <Media omitted>
7/19/23, 17:19 - +254 719 852892: <Media omitted>
7/19/23, 17:45 - MrPatrick: Let’s all adopt this strategy
7/19/23, 18:35 - +254 721 337221: <Media omitted>
7/19/23, 18:35 - +254 721 337221: Kaimosi great things
7/20/23, 15:20 - +254 719 852892: Today in Malava we still went around visiting schools to preach to them the gospel of avocado planting. 1 we visited st Antony Kakoyi sec sch where we met the principal and has given us an appointment to go back n talk to her teachers.
2 we visited Mang'uliro pri where we were able to talk to the deputy head and she also gave us an appointment to still go back to talk to the whole staff
3 At Mang'uliro sec sch we met the deputy principal whereby  we had a great conversation and he has given us an appointment go to his home and check his farm, he is readyto plant with us.
4 At Kakunga pri we met the whole staff whereby we talked to them and we had very great positive response, quite a no of teachers have shown interest in avocado farming.
So generally we got very positive response from all the institutions we visited
7/20/23, 17:54 - +254 113536420: Today in Ogallo farm
7/20/23, 17:54 - +254 113536420: <Media omitted>
7/20/23, 17:54 - +254 113536420: <Media omitted>
7/20/23, 17:54 - +254 113536420: <Media omitted>
7/20/23, 17:54 - +254 113536420: <Media omitted>
7/20/23, 17:54 - +254 113536420: <Media omitted>
7/20/23, 20:46 - MrPatrick: <Media omitted>
7/20/23, 20:47 - MrPatrick: Bee house under construction at Kaimosi home
7/20/23, 20:52 - +254 100323790: This is great
7/21/23, 07:30 - +254 724 957698: <Media omitted>
7/21/23, 07:30 - +254 724 957698: <Media omitted>
7/21/23, 07:30 - +254 724 957698: <Media omitted>
7/21/23, 07:41 - MrPatrick: 👏👏👏
7/21/23, 10:26 - +254 724 850009: <Media omitted>
7/21/23, 11:38 - +254 724 850009: <Media omitted>
7/21/23, 14:05 - MrPatrick: Linci you may give advice
7/21/23, 14:08 - +254 721 337221: How many plants are affected?
7/21/23, 14:09 - +254 724 850009: 1 plant
7/21/23, 14:10 - +254 721 337221: Is there a sign on the other plants sorrounding it?
7/21/23, 14:10 - +254 724 850009: No
7/21/23, 18:56 - MrPatrick: <Media omitted>
7/22/23, 12:28 - MrPatrick: <Media omitted>
7/22/23, 12:28 - MrPatrick: NPK loading for Western avocados
7/22/23, 17:25 - +254 113536420: Fencing and Rootstock preparation in Ogallo farm
7/22/23, 17:25 - +254 113536420: <Media omitted>
7/22/23, 17:25 - +254 113536420: <Media omitted>
7/22/23, 17:25 - +254 113536420: <Media omitted>
7/22/23, 17:25 - +254 113536420: <Media omitted>
7/22/23, 17:25 - +254 113536420: <Media omitted>
7/22/23, 17:26 - +254 113536420: <Media omitted>
7/23/23, 09:08 - MrPatrick: <Media omitted>
7/23/23, 09:08 - MrPatrick: This amazing Sisi ground team!!!!. God bless them
7/23/23, 11:15 - +254 721 337221: <Media omitted>
7/23/23, 11:42 - +254 721 337221: <Media omitted>
7/23/23, 11:48 - +254 721 337221: <Media omitted>
7/23/23, 11:48 - +254 721 337221: <Media omitted>
7/23/23, 11:51 - +254 721 337221: <Media omitted>
7/23/23, 11:51 - +254 721 337221: <Media omitted>
7/23/23, 11:52 - +254 721 337221: <Media omitted>
7/23/23, 11:58 - +254 721 337221: <Media omitted>
7/23/23, 11:58 - +254 721 337221: <Media omitted>
7/23/23, 11:59 - +254 721 337221: <Media omitted>
7/23/23, 11:59 - +254 721 337221: <Media omitted>
7/23/23, 12:00 - +254 721 337221: <Media omitted>
7/23/23, 12:03 - +254 721 337221: <Media omitted>
7/23/23, 12:03 - +254 721 337221: <Media omitted>
7/23/23, 13:16 - +254 714 783208: <Media omitted>
7/23/23, 18:55 - +254 714 783208: <Media omitted>
7/23/23, 19:00 - +254 714 783208: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:16 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:18 - +254 721 337221: <Media omitted>
7/24/23, 08:19 - MrPatrick: 🙏
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 08:20 - +254 721 337221: <Media omitted>
7/24/23, 09:21 - +254 701 843384: <Media omitted>
7/24/23, 09:28 - +254 701 843384: Okalo farm morning prayer
7/24/23, 09:28 - +254 701 843384: <Media omitted>
7/24/23, 09:49 - +254 724 850009: <Media omitted>
7/24/23, 09:49 - +254 721 337221: Great work
7/24/23, 09:53 - MrPatrick: This is amazing!!!
7/24/23, 11:08 - +254 113536420: Ogalo ploughing in progress
7/24/23, 11:09 - +254 113536420: <Media omitted>
7/24/23, 11:09 - +254 113536420: <Media omitted>
7/24/23, 11:09 - +254 113536420: <Media omitted>
7/24/23, 11:09 - +254 113536420: <Media omitted>
7/24/23, 22:33 - +254 722 496898: https://www.businessdailyafrica.com/bd/markets/commodities/us-in-sh22bn-plan-to-help-kenya-grow-avocado-export-market--4310424
7/25/23, 06:33 - MrPatrick: Let us seize the opportunity
7/25/23, 09:00 - +254 113536420: Ogalo cleaning of Drenches and Bushes going on
7/25/23, 09:01 - MrPatrick: <Media omitted>
7/25/23, 09:01 - +254 113536420: <Media omitted>
7/25/23, 09:01 - +254 113536420: <Media omitted>
7/25/23, 09:01 - MrPatrick: Musikoma no jokes
7/25/23, 09:01 - +254 113536420: <Media omitted>
7/25/23, 09:02 - +254 113536420: <Media omitted>
7/25/23, 09:02 - +254 113536420: <Media omitted>
7/25/23, 09:02 - +254 113536420: <Media omitted>
7/25/23, 09:02 - +254 113536420: <Media omitted>
7/25/23, 09:05 - +254 113536420: <Media omitted>
7/25/23, 09:06 - +254 113536420: <Media omitted>
7/25/23, 09:06 - +254 721 337221: Land clearance happening so fast.
7/25/23, 09:22 - MrPatrick: This is greeeat!!
7/25/23, 09:33 - +254 710 364257: <Media omitted>
7/25/23, 09:55 - +254 721 337221: Tom great work
7/25/23, 11:01 - +254 719 852892: <Media omitted>
7/25/23, 11:01 - +254 719 852892: <Media omitted>
7/25/23, 11:01 - +254 719 852892: <Media omitted>
7/25/23, 11:01 - +254 719 852892: <Media omitted>
7/25/23, 11:01 - +254 719 852892: <Media omitted>
7/25/23, 12:21 - +254 100323790: <Media omitted>
7/25/23, 15:09 - +254 100323790: <Media omitted>
7/25/23, 16:21 - MrPatrick: Thanks much Ambassador
7/25/23, 19:01 - +254 113536420: Ogalo rootstock preparation on progress
7/25/23, 19:03 - +254 113536420: <Media omitted>
7/25/23, 19:03 - +254 113536420: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/25/23, 19:47 - +254 721 337221: <Media omitted>
7/26/23, 11:54 - +254 100323790: <Media omitted>
7/26/23, 12:38 - MrPatrick: This is great
7/26/23, 21:09 - +254 113536420: Ogalo weeding and clearence of bush is continue.
7/26/23, 21:31 - +254 113536420: <Media omitted>
7/26/23, 21:36 - +254 113536420: <Media omitted>
7/26/23, 21:36 - +254 113536420: <Media omitted>
7/26/23, 21:42 - MrPatrick: Keep up the good work
7/27/23, 10:56 - +254 724 850009: <Media omitted>
7/27/23, 11:26 - MrPatrick: 👏👏👏
7/27/23, 11:31 - +254 100323790: 👍🏻
7/28/23, 10:21 - +254 113536420: Ogalo weeding and Bush is still going on
7/28/23, 10:22 - +254 113536420: <Media omitted>
7/28/23, 10:22 - +254 113536420: <Media omitted>
7/28/23, 10:22 - +254 113536420: <Media omitted>
7/28/23, 10:23 - +254 113536420: <Media omitted>
7/28/23, 10:23 - +254 113536420: <Media omitted>
7/28/23, 10:23 - +254 113536420: <Media omitted>
7/28/23, 10:23 - +254 113536420: <Media omitted>
7/28/23, 10:23 - +254 722 709250: 🙏
7/28/23, 10:24 - +254 113536420: <Media omitted>
7/28/23, 17:28 - +254 113536420: <Media omitted>
7/29/23, 11:37 - +254 790 148692: <Media omitted>
7/29/23, 11:37 - +254 790 148692: <Media omitted>
7/29/23, 11:51 - MrPatrick: That is interesting!!!
7/29/23, 12:52 - +254 790 148692: <Media omitted>
7/29/23, 12:52 - +254 790 148692: <Media omitted>
7/29/23, 12:52 - +254 790 148692: <Media omitted>
7/29/23, 12:53 - +254 790 148692: <Media omitted>
7/29/23, 12:53 - +254 790 148692: <Media omitted>
7/29/23, 12:54 - +254 790 148692: <Media omitted>
7/29/23, 13:04 - +254 722 709250: Always remember, cheap/free is expensive. 
Quality and reliability has    a cost.
7/29/23, 13:10 - +254 790 148692: Yea
7/29/23, 16:21 - +254 790 148692: <Media omitted>
7/29/23, 16:21 - +254 790 148692: <Media omitted>
7/29/23, 16:21 - +254 790 148692: <Media omitted>
7/29/23, 16:23 - +254 790 148692: <Media omitted>
7/29/23, 16:23 - +254 790 148692: <Media omitted>
7/29/23, 16:23 - +254 790 148692: <Media omitted>
7/29/23, 16:32 - +254 790 148692: <Media omitted>
7/29/23, 16:32 - +254 790 148692: <Media omitted>
7/29/23, 16:32 - +254 790 148692: <Media omitted>
7/29/23, 16:36 - +254 790 148692: <Media omitted>
7/29/23, 16:36 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 16:37 - +254 790 148692: <Media omitted>
7/29/23, 18:02 - +254 113536420: Ogalo we have received 42 bags of rootstock from Guardian Office Bumala
7/29/23, 18:02 - +254 113536420: Ogalo Demo farm, Phase One A and B blocks is now through, ready to plant
7/29/23, 18:02 - +254 113536420: Fencing of Nursery shade and seedbed in progress
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:03 - +254 113536420: <Media omitted>
7/29/23, 18:30 - +254 721 337221: <Media omitted>
7/29/23, 18:30 - +254 721 337221: <Media omitted>
7/29/23, 18:30 - +254 721 337221: <Media omitted>
7/29/23, 18:30 - +254 721 337221: <Media omitted>
7/29/23, 18:30 - +254 721 337221: Good
7/29/23, 18:31 - +254 721 337221: Good one
7/29/23, 18:33 - +254 721 337221: Great team
7/30/23, 04:11 - MrPatrick removed +254 790 433944
7/30/23, 04:14 - MrPatrick: Home looking great
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 07:23 - +254 790 148692: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 721 337221: Great
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:07 - +254 742 254722: <Media omitted>
7/31/23, 08:11 - MrPatrick: Very encouraging report
7/31/23, 08:23 - +254 721 337221: <Media omitted>
7/31/23, 08:24 - +254 721 337221: Faith and Hudson great work you did at chiefs place yesterday.
7/31/23, 08:31 - MrPatrick: 👍🏽
7/31/23, 12:33 - +254 701 843384: <Media omitted>
7/31/23, 12:33 - +254 701 843384: <Media omitted>
7/31/23, 12:34 - +254 721 337221: <Media omitted>
7/31/23, 13:12 - MrPatrick: 🙏
7/31/23, 14:36 - +254 701 843384: <Media omitted>
7/31/23, 14:36 - +254 701 843384: <Media omitted>
7/31/23, 14:39 - MrPatrick: Grow Ogalo grow
7/31/23, 14:43 - +254 703 491022: Silas
7/31/23, 14:46 - +254 113536420: Our seedlings in Ogallo Nursery are showing New shoots, between
4 and 5 weeks old acclimatizing
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:17 - +254 113536420: <Media omitted>
7/31/23, 15:20 - +254 721 337221: Very encouraging
7/31/23, 15:20 - +254 721 337221: Do we have rains?
7/31/23, 20:14 - +254 113536420: There's no rain but kuna dalili ya mawingu.
7/31/23, 20:19 - +254 721 337221: Miti ziko na maji?
7/31/23, 21:50 - +254 721 337221: A very sad story. Unfortunately I had to face it head-on. This was the case of an export company called Kilimambogo packers stationed in Thika, trying to steal my Hass avocados in a clever way. What saved me was both my sixth sense and subconscious mind. It was the kind of theft that would have made me almost lose my mind  if I discovered much later.

They plucked my Hass avocados today at the agreed price of 85/- per kg. We weighed all the 120 crates. They had an electronic which all of us trust. I have never questioned an electronic weighing scale.

I was abit surprised that all my avocados weighed about 1,200kg. For some reason as the process finished and the reality was eating me up, I decided to do the unthinkable, weigh myself. I weighed 75kg, but in a matter of seconds it dawned on me that my weight is 85kg and not 75kg. I must have gone berserk. 

By this time the weighing scale had already been taken to the lorry in preparation to leave. I rushed to the vehicle and asked for the scale because my weight is not 75kg. They took it out. Put it on a flat surface, and this time round I weighed 90kg. I shouted, I don't weigh 90kg. Everyone smelt a rat. 

I told  the supervisor by name Stephen, that this was a police case. My head was asking me, how many farmers had fleeced like that. We rushed to the police station. We came back with the police officer and said we take weight of one crate. This time round the machine was working well and gave us a correct weight, though double what had been declared before. My hand spring balance matched the weight.

It was now an easy case which the officer termed a fraud. My entire sale had been halved. Instead of 1,200kg, it should have been 2,400kg. They paid that without an argument. 

We spared them the  trouble of the lorry being impounded and all the produce going to waste plus a lengthy court case.

How many farmers have they stolen from in Embu which is their main domain? That is what a peasant farmer is going through in the hands of a trusted exporter who is respected for having a fleet of lorries.
7/31/23, 23:24 - MrPatrick: Very sad indeed
8/1/23, 06:54 - +254 724 957698: This is  common practice among all produce buyers. In the maize sector, this has led to farmers abandoning maize farming altogether. From this example, the only way out is for producers to band together and do everything cooperatively.  This will call for strong cooperatives that can stand up to some of these rascals.
8/1/23, 07:16 - MrPatrick: 👍🏽
8/1/23, 07:54 - +254 100323790: Absolutely chairman 👏
8/1/23, 09:56 - +254 710 338421: Very sad indeed, underscores the need to develop joint strategic approach.
8/1/23, 16:54 - +254 714 783208: <Media omitted>
8/2/23, 12:21 - +254 113536420: Ogalo preparation of Phase One C blocks is on going
8/2/23, 12:22 - +254 113536420: <Media omitted>
8/2/23, 12:22 - +254 113536420: <Media omitted>
8/2/23, 12:22 - +254 113536420: <Media omitted>
8/2/23, 14:27 - +254 724 850009: <Media omitted>
8/2/23, 19:58 - +254 714 783208: <Media omitted>
8/2/23, 20:00 - +254 714 783208: Tomorrow I will going round distributing some forms to all the stations
8/2/23, 20:05 - +254 721 337221: Ok great
8/3/23, 17:16 - MrPatrick: <Media omitted>
8/3/23, 17:16 - MrPatrick: Good job in Kimilili Hudson
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:28 - +254 790 148692: <Media omitted>
8/3/23, 17:29 - +254 790 148692: <Media omitted>
8/3/23, 17:29 - +254 790 148692: <Media omitted>
8/3/23, 17:29 - +254 790 148692: <Media omitted>
8/3/23, 17:29 - +254 790 148692: <Media omitted>
8/3/23, 17:29 - +254 790 148692: <Media omitted>
8/4/23, 13:24 - +254 724 850009: <Media omitted>
8/4/23, 20:16 - MrPatrick: <Media omitted>
8/5/23, 16:20 - +254 724 850009: <Media omitted>
8/5/23, 17:24 - MrPatrick: Bee house waaaaaa!!
8/5/23, 18:01 - MrPatrick: <Media omitted>
8/5/23, 18:01 - MrPatrick: <Media omitted>
8/5/23, 18:01 - MrPatrick: Congrats Hudson for beautiful work in Kimilili
8/5/23, 18:07 - +254 113536420: Ogalo team at finishing Time
8/5/23, 18:07 - +254 113536420: Ogalo indication of trees measurements is going on
8/5/23, 18:07 - +254 113536420: Ogalo yesterday we received 2 Lorries of Sand and in the morning
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:07 - +254 113536420: <Media omitted>
8/5/23, 18:08 - +254 113536420: <Media omitted>
8/5/23, 18:08 - +254 113536420: <Media omitted>
8/6/23, 08:28 - +254 721 337221: <Media omitted>
8/6/23, 08:28 - +254 721 337221: <Media omitted>
8/6/23, 08:28 - +254 721 337221: <Media omitted>
8/6/23, 09:18 - MrPatrick: Good work Saleh and Julius
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 09:22 - +254 721 337221: <Media omitted>
8/6/23, 11:55 - +254 724 850009: <Media omitted>
8/6/23, 12:13 - +254 724 850009: <Media omitted>
8/6/23, 12:42 - +254 724 850009: <Media omitted>
8/6/23, 15:04 - +254 113536420: We add working tools in Ogalo
8/6/23, 15:04 - +254 113536420: <Media omitted>
8/6/23, 15:05 - +254 113536420: <Media omitted>
8/6/23, 15:05 - +254 113536420: <Media omitted>
8/6/23, 15:05 - +254 113536420: <Media omitted>
8/6/23, 15:05 - +254 113536420: <Media omitted>
8/6/23, 15:05 - +254 113536420: <Media omitted>
8/6/23, 15:39 - +254 721 337221: Great team
8/7/23, 11:34 - +254 701 843384: <Media omitted>
8/7/23, 11:34 - +254 701 843384: <Media omitted>
8/7/23, 11:34 - +254 701 843384: <Media omitted>
8/7/23, 11:34 - +254 721 337221: This is the right stage to transplant
8/7/23, 15:37 - +254 733 812060: <Media omitted>
8/7/23, 15:41 - +254 733 812060: I have two acres of land ready for preparation of ridges in Maseno. 
Director . When you come on 9th please advise the Sisi agent Makale 0716384248 how to orient the ridges in relation to the gradient and sunlight. Makale was trained by Hudson on how to prepare the ridges.
Several other farmers are ready
8/7/23, 15:57 - +254 701 843384: <Media omitted>
8/7/23, 15:58 - +254 701 843384: <Media omitted>
8/7/23, 18:14 - +254 733 812060: Could you ask visit the demonstration farm in Nyawita and advise on husbandry. Some plants have adopted others seem to struggle. 
Please advise on watering, pruning and numbering of the plants.
8/7/23, 18:17 - +254 721 337221: Hallo Sir Tongoi,
Is this your farm in maseno?
8/7/23, 18:18 - +254 721 337221: I would like to see the progress before we talk about what you have raised above, I will liase with the CEO to see how we can plan on logistics
8/7/23, 18:24 - +254 728 812060: This is Tongoi.
Yes I have two farms in Maseno.
The demonstration farm that already has 225 Hass Avocado in Maseno(Nyawita) which is where I need the support and an additional two acres in Maseno (Car wash)that I have harvested Maize and is now ready for preparation of the ridges. I need advise on how they should be oriented. This should be an additional 250 seedlings for me alone. 
I understand ChIrman will be visiting the Cooperative on Wednesday 9th August. 17 other farmers are ready to prepare their land.
8/7/23, 18:27 - +254 721 337221: Let him advise on the the urgency and I can avail myself
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:15 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 11:16 - +254 790 148692: <Media omitted>
8/8/23, 15:39 - +254 724 850009: <Media omitted>
8/8/23, 19:06 - +254 742 254722: <Media omitted>
8/8/23, 19:07 - +254 742 254722: <Media omitted>
8/8/23, 19:57 - +254 113536420: Bedding in Phase One C blocks is going on in Ogalo Demo farm
8/8/23, 19:59 - +254 113536420: Pegging in our Demo farm Ogalo, 5 blocks of Phase One A and B will be through by tomorrow
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/8/23, 20:01 - +254 113536420: <Media omitted>
8/9/23, 09:42 - +254 742 254722: <Media omitted>
8/9/23, 09:42 - +254 742 254722: <Media omitted>
8/9/23, 09:42 - +254 742 254722: <Media omitted>
8/9/23, 09:42 - +254 742 254722: <Media omitted>
8/9/23, 09:46 - +254 742 254722: <Media omitted>
8/9/23, 16:04 - +254 728 812060: <Media omitted>
8/9/23, 16:05 - +254 742 254722: <Media omitted>
8/9/23, 16:05 - +254 742 254722: <Media omitted>
8/9/23, 16:05 - +254 742 254722: <Media omitted>
8/9/23, 16:05 - +254 742 254722: <Media omitted>
8/9/23, 16:05 - +254 742 254722: <Media omitted>
8/9/23, 16:07 - +254 728 812060: One of my trees has died. 
My team waited for the visit today as earlier promised but we are yet to see this materialize.
My Cooperative members are getting discouraged. The pattern of promises without execution is what they are used to .

30 farmers are read to plants 17 are ready for beehives.

Please advise?
8/9/23, 16:08 - +254 728 812060: This is the dead trees
8/9/23, 16:18 - MrPatrick: On my way to Maseno from Kisumu
8/9/23, 16:29 - +254 733 812060: Please confirm if you have been in touch with Adam. He has been looking for you.
8/9/23, 16:34 - MrPatrick: He is calling you also
8/9/23, 19:01 - +254 724 850009: <Media omitted>
8/9/23, 19:12 - +254 721 337221: Good, did the seedlings come?
8/9/23, 19:16 - +254 724 850009: Not yet
8/9/23, 20:04 - MrPatrick: <Media omitted>
8/9/23, 20:04 - MrPatrick: <Media omitted>
8/9/23, 21:13 - +254 722 496898: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:16 - MrPatrick: <Media omitted>
8/9/23, 21:20 - MrPatrick: This is interesting!!! We have to up our game team
8/9/23, 21:24 - +254 721 337221: This was my dream some 6yrs back, I wish I had met Kisia by then, but I still believe it's not late we are going to change our region
8/9/23, 21:26 - MrPatrick: 👍🏽👍🏽👍🏽
8/9/23, 21:30 - MrPatrick: null
8/9/23, 21:30 - MrPatrick: Our Engineer making it happen at Musikoma
8/9/23, 21:30 - +254 100323790: 👏👏
8/10/23, 11:03 - +254 113536420: This is our Phase One C blocks in Ogalo
8/10/23, 12:39 - +254 724 850009: <Media omitted>
8/10/23, 15:43 - MrPatrick: <Media omitted>
8/10/23, 16:53 - +254 742 254722: <Media omitted>
8/10/23, 17:41 - +254 722 502957: <Media omitted>
8/10/23, 17:53 - MrPatrick: Great work Haron
8/10/23, 18:56 - +254 721 337221: Kudos Timo
8/10/23, 19:00 - MrPatrick: Great work Timo
8/10/23, 19:27 - +254 100323790: Good work team malava keep it up👏👏
8/10/23, 21:59 - MrPatrick: <Media omitted>
8/10/23, 21:59 - MrPatrick: Great work Musikoma
8/11/23, 14:22 - +254 722 502957: <Media omitted>
8/11/23, 16:06 - +254 721 337221: <Media omitted>
8/11/23, 16:06 - +254 721 337221: <Media omitted>
8/11/23, 16:06 - +254 721 337221: <Media omitted>
8/11/23, 16:06 - +254 721 337221: Hudson and Solomon great things there. Make the orchard the best.
8/11/23, 16:06 - +254 721 337221: Bungoma itatii
8/11/23, 17:08 - MrPatrick: Proud of this wonderful work
8/11/23, 17:08 - MrPatrick: Timo and Adoli good work
8/11/23, 17:11 - +254 722 709250 started a call
8/12/23, 10:13 - +254 721 337221: <Media omitted>
8/12/23, 10:13 - +254 721 337221: <Media omitted>
8/12/23, 10:14 - +254 721 337221: <Media omitted>
8/12/23, 10:14 - +254 721 337221: <Media omitted>
8/12/23, 14:24 - +254 722 496898: <Media omitted>
8/12/23, 19:33 - MrPatrick removed +254 716 384248
8/12/23, 19:32 - +254 716 384248 started a call
8/13/23, 10:16 - MrPatrick: https://www.facebook.com/100080205698712/posts/pfbid06xxhSvePs9n8YxRC4TJdVTbDkAG4qGxewMC5en7NcktNQRPXr4XUwo3VTsRsLViWl/

I have encouraged youth to embrace agriculture more so avocado farming. This is the surest way of solving the unemployment crisis in the country. 

The crop, now being referred to as green gold, is fetching good money both in local and international markets.

Delighted to attend the launch of SiSi Village Produce, a non-governmental organization that has set base at Musikoma Ward, Kanduyi Constituency. 

The group is empowering youth through the cultivation of a new breed of Avocado called Hass Avocado; a pest-resistant crop that favors our soil and has rich nutritional value.

Patrick Kisia, the CEO, mentioned they have over 100,000 Hass Avocado seedlings available for motivated young individuals interested in venturing into avocado farming.

Joined by colleague MP Jack Wamboka (Bumula), Maxwell Shamalla (ex-EALA MP), and Sande Onyolo, a political leader, among others.

#KanduyiArising

*Wakili John Makali, MP*
*Kanduyi Constituency*
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:44 - +254 721 337221: <Media omitted>
8/13/23, 10:45 - +254 721 337221: <Media omitted>
8/13/23, 10:45 - +254 721 337221: <Media omitted>
8/13/23, 10:45 - +254 721 337221: <Media omitted>
8/13/23, 10:45 - +254 721 337221: <Media omitted>
8/13/23, 10:45 - +254 721 337221: <Media omitted>
8/13/23, 11:01 - +254 721 337221: <Media omitted>
8/13/23, 11:01 - +254 721 337221: Sisi the brand to watch
8/13/23, 11:07 - +254 722 502957: <Media omitted>
8/13/23, 11:07 - +254 721 337221: Great things Timo
8/13/23, 13:12 - MrPatrick added +254 723 156195 and +254 731 619860
8/13/23, 13:13 - MrPatrick: Let’s welcome Karen Wakhungu of the Musikoma Avocado Promotion Centre
8/13/23, 13:16 - MrPatrick: Great work Timo. Kazi kwa Sisi ground team
8/13/23, 13:39 - +254 723 156195: Thanks for the Add.
8/13/23, 16:40 - MrPatrick: <Media omitted>
8/13/23, 16:40 - MrPatrick: Timo in Kimilili
8/13/23, 17:10 - +254 722 502957: Tuko kimilili
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: <Media omitted>
8/13/23, 17:16 - MrPatrick: Cooperative in Kisumu
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: <Media omitted>
8/13/23, 17:17 - MrPatrick: Maseno onboarding progress
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:45 - +254 721 337221: <Media omitted>
8/13/23, 17:46 - +254 721 337221: Hygiene needs to be done as a matter of urgency, irrigation also needs to be followed as the farm is murrum at some places
8/13/23, 20:58 - +254 733 812060: Thank you for the visit and advise. I will be present from next week for two weeks to to supervise the land preparation.
8/13/23, 22:21 - +254 721 337221: Always on the look for better orchards
8/14/23, 00:21 - MrPatrick: https://www.facebook.com/100080205698712/posts/pfbid06xxhSvePs9n8YxRC4TJdVTbDkAG4qGxewMC5en7NcktNQRPXr4XUwo3VTsRsLViWl/

I have encouraged youth to embrace agriculture more so avocado farming. This is the surest way of solving the unemployment crisis in the country. 

The crop, now being referred to as green gold, is fetching good money both in local and international markets.

Delighted to attend the launch of SiSi Village Produce, a non-governmental organization that has set base at Musikoma Ward, Kanduyi Constituency. 

The group is empowering youth through the cultivation of a new breed of Avocado called Hass Avocado; a pest-resistant crop that favors our soil and has rich nutritional value.

Patrick Kisia, the CEO, mentioned they have over 100,000 Hass Avocado seedlings available for motivated young individuals interested in venturing into avocado farming.

Joined by colleague MP Jack Wamboka (Bumula), Maxwell Shamalla (ex-EALA MP), and Sande Onyolo, a political leader, among others.

#KanduyiArising

*Wakili John Makali, MP*
*Kanduyi Constituency*
8/14/23, 08:26 - +254 721 337221: <Media omitted>
8/14/23, 08:41 - +254 724 850009: <Media omitted>
8/14/23, 08:42 - +254 721 337221: <Media omitted>
8/14/23, 09:12 - MrPatrick: Is it fully planted now?
8/14/23, 09:15 - +254 721 337221: It was fully planted on the launch day.
8/14/23, 09:24 - MrPatrick: 👏👏👏
8/14/23, 10:13 - +254 701 843384: <Media omitted>
8/14/23, 10:16 - +254 721 337221: Great team
8/14/23, 10:32 - +254 113536420: Team Ogalo at work
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:32 - +254 113536420: <Media omitted>
8/14/23, 10:37 - MrPatrick: This is beautiful!!!
8/14/23, 13:14 - +254 722 496898: <Media omitted>
8/14/23, 13:19 - MrPatrick: Avomeru are our Tanzania partners
8/14/23, 20:03 - +254 724 850009: <Media omitted>
8/14/23, 20:03 - +254 724 850009: <Media omitted>
8/14/23, 20:03 - +254 724 850009: <Media omitted>
8/14/23, 20:03 - +254 724 850009: <Media omitted>
8/14/23, 20:03 - +254 724 850009: At Musikoma educating KeNHA team about hass a avocado 🥑 and it's benefits
8/14/23, 20:57 - +254 100323790: Heko solo keep the spirit up. Good work👍
8/15/23, 00:47 - MrPatrick: <Media omitted>
8/15/23, 00:47 - MrPatrick: Linci teaching recruited agents at Kimilili Centre
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:51 - MrPatrick: <Media omitted>
8/15/23, 06:53 - MrPatrick: Linci training field agents at Kimilili Avocado Promotion Centre
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:25 - +254 721 337221: <Media omitted>
8/15/23, 09:26 - +254 721 337221: <Media omitted>
8/15/23, 09:26 - +254 721 337221: <Media omitted>
8/15/23, 09:26 - +254 721 337221: <Media omitted>
8/15/23, 09:26 - +254 721 337221: <Media omitted>
8/15/23, 09:26 - +254 721 337221: <Media omitted>
8/15/23, 09:28 - +254 113536420: Ogalo Demo farm, Phase One C blocks, will be through by tomorrow
8/15/23, 09:28 - +254 113536420: <Media omitted>
8/15/23, 09:28 - +254 113536420: <Media omitted>
8/15/23, 09:28 - +254 113536420: <Media omitted>
8/15/23, 09:28 - +254 113536420: <Media omitted>
8/15/23, 09:28 - +254 113536420: <Media omitted>
8/15/23, 10:07 - +254 113536420: <Media omitted>
8/15/23, 10:15 - +254 721 337221: <Media omitted>
8/15/23, 10:44 - MrPatrick: This is amazing !!!
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 13:34 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:23 - +254 721 337221: <Media omitted>
8/15/23, 16:28 - MrPatrick: <Media omitted>
8/15/23, 16:28 - MrPatrick: <Media omitted>
8/15/23, 16:29 - MrPatrick: Training agents at our Malava avocado station
8/15/23, 17:17 - +254 724 850009: <Media omitted>
8/15/23, 18:01 - MrPatrick: Be sure to spray water, not pour
8/15/23, 19:15 - +254 722 709250: Sure Sure.
8/15/23, 21:48 - MrPatrick: <Media omitted>
8/15/23, 21:48 - MrPatrick: Tree planting launched in Ogalo
8/15/23, 21:56 - MrPatrick: <Media omitted>
8/15/23, 21:56 - MrPatrick: Tree planting launched in Ogalo
8/15/23, 21:59 - MrPatrick: <Media omitted>
8/15/23, 22:00 - MrPatrick: <Media omitted>
8/15/23, 22:00 - MrPatrick: <Media omitted>
8/15/23, 22:00 - MrPatrick: <Media omitted>
8/15/23, 22:00 - MrPatrick: <Media omitted>
8/16/23, 06:55 - MrPatrick: <Media omitted>
8/16/23, 06:55 - MrPatrick: <Media omitted>
8/16/23, 06:55 - MrPatrick: <Media omitted>
8/16/23, 06:55 - MrPatrick: Maseno is loading
8/16/23, 06:55 - MrPatrick: <Media omitted>
8/16/23, 18:34 - +254 113536420: Ogalo bedding is done today
8/16/23, 18:41 - +254 113536420: Ogalo planting in progress
8/16/23, 18:41 - +254 113536420: <Media omitted>
8/16/23, 18:41 - +254 113536420: <Media omitted>
8/16/23, 18:41 - +254 113536420: <Media omitted>
8/16/23, 18:41 - +254 113536420: <Media omitted>
8/16/23, 18:43 - +254 113536420: <Media omitted>
8/16/23, 18:44 - +254 113536420: <Media omitted>
8/16/23, 18:44 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:47 - +254 113536420: <Media omitted>
8/16/23, 18:49 - +254 113536420: <Media omitted>
8/16/23, 18:49 - +254 113536420: <Media omitted>
8/16/23, 18:49 - +254 113536420: <Media omitted>
8/16/23, 18:50 - +254 113536420: <Media omitted>
8/16/23, 19:50 - +254 100323790: <Media omitted>
8/16/23, 21:39 - MrPatrick: Elijah is a good communicator. The recording will be shared
8/17/23, 08:25 - +254 728 812060: When can QA manager visit the farm and identify the trees. I am installing a drip line irrigation. Should I wait until we replace the non-performing trees ?
8/17/23, 10:44 - +254 113536420: Ogalo planting is on going at the second day
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/17/23, 10:47 - +254 113536420: <Media omitted>
8/18/23, 15:35 - +254 113536420: Ogalo farm, PHASE ONE; A and B of 5 blocks is now through.
Tomorrow we start weeding imediately
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 15:36 - +254 113536420: <Media omitted>
8/18/23, 17:28 - +254 724 850009: <Media omitted>
8/18/23, 17:29 - +254 721 337221: "Avocado market goes from one extreme to the next" - https://go.shr.lc/3DY9AwM
8/18/23, 18:18 - +254 721 337221: <Media omitted>
8/18/23, 18:18 - +254 721 337221: Hudson now you got it, great beds. standard.
8/18/23, 18:20 - +254 721 337221: <Media omitted>
8/18/23, 18:20 - +254 721 337221: Great things
8/19/23, 04:50 - MrPatrick: Great work Saleh
8/19/23, 08:41 - +254 113536420: Ogalo weeding and irrigation activity is taking place
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:42 - +254 113536420: <Media omitted>
8/19/23, 08:45 - +254 113536420: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: <Media omitted>
8/19/23, 14:14 - MrPatrick: Sisi Village Produce CSR Program
8/19/23, 14:17 - MrPatrick: <Media omitted>
8/19/23, 14:17 - MrPatrick: <Media omitted>
8/19/23, 14:17 - MrPatrick: <Media omitted>
8/19/23, 14:18 - MrPatrick: <Media omitted>
8/19/23, 14:18 - MrPatrick: <Media omitted>
8/19/23, 14:18 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:22 - MrPatrick: <Media omitted>
8/19/23, 14:23 - MrPatrick: <Media omitted>
8/19/23, 14:23 - MrPatrick: <Media omitted>
8/19/23, 14:52 - +254 721 337221: <Media omitted>
8/19/23, 14:52 - +254 721 337221: Am worried about the handling of this seedlings.
8/19/23, 15:33 - MrPatrick: This is not good packing
8/19/23, 15:53 - +254 722 502957: Packing not good
8/19/23, 16:24 - +254 721 337221: Timo can we do a training on packing. Can we standardize how seedlings are supposed to be packed?
8/19/23, 16:44 - MrPatrick: Our people know how to pack sure. I wonder what happened now!!!
8/19/23, 17:19 - +254 722 502957: <Media omitted>
8/20/23, 08:42 - MrPatrick: <Media omitted>
8/20/23, 08:42 - MrPatrick: Section of the children on the retreat
8/20/23, 09:33 - +254 701 843384: <Media omitted>
8/20/23, 09:44 - +254 100323790: Wonderful 👏👏👏
8/20/23, 15:42 - MrPatrick: Kudos Henry for initiating the children’s retreat
8/20/23, 22:10 - +254 722 709250: Mentoring the future nation. Thumbs-up to those involved.
8/20/23, 22:32 - +254 723 156195: Wonderfull 🙏
8/21/23, 09:33 - +254 113536420: Ogalo team at the morning meeting
8/21/23, 09:33 - +254 113536420: Irrigation at Ogalo farm
8/21/23, 09:34 - +254 113536420: <Media omitted>
8/21/23, 09:34 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:37 - +254 113536420: <Media omitted>
8/21/23, 09:40 - +254 113536420: <Media omitted>
8/21/23, 09:40 - +254 113536420: <Media omitted>
8/21/23, 09:40 - +254 113536420: <Media omitted>
8/21/23, 09:40 - +254 113536420: <Media omitted>
8/21/23, 09:41 - +254 113536420: <Media omitted>
8/21/23, 12:30 - +254 701 843384: <Media omitted>
8/21/23, 21:09 - +254 100323790: <Media omitted>
8/22/23, 16:06 - +254 742 254722: <Media omitted>
8/22/23, 16:06 - +254 742 254722: <Media omitted>
8/22/23, 16:06 - +254 742 254722: <Media omitted>
8/22/23, 16:31 - MrPatrick: 👏👏👏
8/22/23, 18:54 - +254 113536420: Ogalo packing is on going
8/22/23, 18:57 - +254 113536420: Weeding and irrigation is in progress
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/22/23, 18:58 - +254 113536420: <Media omitted>
8/23/23, 11:32 - +254 728 812060: <Media omitted>
8/23/23, 17:59 - +254 728 812060: <Media omitted>
8/23/23, 18:00 - +254 728 812060: <Media omitted>
8/23/23, 18:00 - +254 728 812060: Maseno Demo farm
8/23/23, 18:00 - +254 728 812060: <Media omitted>
8/23/23, 19:26 - +254 113536420: Transplanting in Ogalo is starting
8/23/23, 19:31 - +254 728 812060: Does anyone have a market for 90kgs of these Green Onions?
8/23/23, 19:31 - +254 113536420: <Media omitted>
8/23/23, 19:31 - +254 113536420: <Media omitted>
8/23/23, 19:31 - +254 113536420: <Media omitted>
8/23/23, 19:47 - +254 710 338421: Dr, try Kibuye market on Sunday.
8/23/23, 21:10 - MrPatrick: We need them at Musikoma
8/23/23, 21:11 - MrPatrick: 👏👏👏
8/23/23, 21:35 - +254 722 502957: Jaribu kifunika begu na musanga suaree
8/23/23, 21:50 - +254 728 812060: How much can they pay?  Would they collect?
8/24/23, 10:08 - +254 701 843384: <Media omitted>
8/24/23, 10:09 - +254 701 843384: <Media omitted>
8/24/23, 11:15 - MrPatrick: 👏👏👏
8/24/23, 11:39 - +254 113536420: This message was deleted
8/24/23, 12:28 - +254 701 843384: <Media omitted>
8/25/23, 19:59 - +254 719 852892: <Media omitted>
8/25/23, 20:14 - +254 719 852892: This message was deleted
8/25/23, 20:22 - +254 719 852892: <Media omitted>
8/25/23, 20:26 - +254 100323790: Good demonstration 👍
8/26/23, 07:31 - +254 722 496898: <Media omitted>
8/26/23, 19:47 - +254 113536420: Mulching in Ogalo is taking place
8/26/23, 19:49 - +254 113536420: <Media omitted>
8/26/23, 19:49 - +254 113536420: <Media omitted>
8/26/23, 19:49 - +254 113536420: <Media omitted>
8/26/23, 19:49 - +254 113536420: <Media omitted>
8/26/23, 19:49 - +254 113536420: <Media omitted>
8/26/23, 19:50 - +254 113536420: <Media omitted>
8/26/23, 19:50 - +254 113536420: <Media omitted>
8/26/23, 21:41 - MrPatrick: 👏👏👏
8/26/23, 21:44 - MrPatrick: Ambassador you may post the next pages
8/27/23, 18:48 - MrPatrick: <Media omitted>
8/27/23, 18:49 - MrPatrick: Farmer in Bungoma bringing down 3 acres of banana plantation to plant avocado!!!
8/27/23, 19:03 - +254 722 709250: This is going to be the story across the county
8/27/23, 19:18 - MrPatrick: This is challenging!!
8/28/23, 08:23 - +254 721 337221: <Media omitted>
8/28/23, 09:45 - +254 721 337221: <Media omitted>
8/28/23, 16:16 - +254 113536420: Ogalo mulching and transplanting is going on
8/28/23, 16:17 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:18 - +254 113536420: <Media omitted>
8/28/23, 16:22 - +254 113536420: <Media omitted>
8/28/23, 16:22 - +254 113536420: <Media omitted>
8/28/23, 16:24 - +254 721 337221: It's ok but make sure water doesn't sit for long on the grass, the essence is to keep the soil moist.
8/28/23, 16:47 - +254 113536420: Ok
8/28/23, 19:53 - +254 742 254722: <Media omitted>
8/28/23, 19:57 - +254 742 254722: <Media omitted>
8/28/23, 19:58 - +254 742 254722: <Media omitted>
8/28/23, 19:58 - +254 742 254722: <Media omitted>
8/28/23, 19:59 - +254 100323790: Absolutely
8/28/23, 20:31 - +254 742 254722: <Media omitted>
8/28/23, 20:36 - MrPatrick: Very good work in Maseno!!
8/28/23, 20:40 - +254 721 337221: Excellence
8/29/23, 10:38 - +254 113536420: Hygiene activity in Ogalo is going on
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:40 - +254 113536420: <Media omitted>
8/29/23, 10:42 - +254 113536420: <Media omitted>
8/29/23, 10:43 - +254 113536420: <Media omitted>
8/29/23, 10:53 - MrPatrick: Happy with Saleh and Julius for confronting the challenges
8/29/23, 10:57 - +254 742 254722: <Media omitted>
8/29/23, 10:58 - +254 742 254722: <Media omitted>
8/29/23, 10:58 - +254 742 254722: <Media omitted>
8/29/23, 10:59 - +254 742 254722: <Media omitted>
8/29/23, 10:59 - +254 742 254722: <Media omitted>
8/29/23, 11:04 - MrPatrick: Very proud of Haron and Dickens for facing and surmounting the challenges in rocky Maseno
8/29/23, 11:24 - +254 742 254722: Good morning 🌄 sir so far I have seven young men who are undergoing the process of beds formation plus other basic knowledge here in maseno we pray God to sustain them with His knowledge and I believe their lives will never remain the same sir.
8/29/23, 11:26 - MrPatrick: That is great. Engage with the farmers to pay them reliably
8/29/23, 11:27 - +254 721 337221: As the saying goes, " Teach someone to teach someone" 
It is a legacy.
8/29/23, 12:57 - MrPatrick: <Media omitted>
8/29/23, 12:58 - MrPatrick: Musikoma on fire!!
8/29/23, 13:15 - MrPatrick: <Media omitted>
8/29/23, 19:43 - +254 100323790: Good Business keep it high👏👏
"""
cleaned_output = clean_chat(original_chat)

# Set the path where you want to save the cleaned output
output_folder = "/home/lennox/chatbot/cleaned"
output_file_path = f"{output_folder}/cleaned_output.txt"

# Save the cleaned output to the file
save_to_file(cleaned_output, output_file_path)

print(f"Cleaned output saved to: {output_file_path}")
