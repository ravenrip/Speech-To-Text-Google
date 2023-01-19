import difflib
import string

import pandas as pd

text_to_speech0 = "I have the pleasure to present to you dr. Martin Luther King Jr."
text_to_speech1 = "I am happy to join with you today. In what will go down in history as the greatest demonstration for freedom in the history of our nation,"
text_to_speech2 = "five, score years ago, a great American in whose symbolic Shadow We Stand today. signed the Emancipation Proclamation, this momentous decree came As a great Beacon, Light Of Hope to millions of negro slaves. Who had been seared in the Flames of withering Injustice, it came as a joyous Daybreak. To win the long night of their captivity. But 100 years later. The Negro still is not free. 100 years later. The life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination 100 years later. The Negro lives on a lonely island of poverty. In the midst of a vast, ocean of material Prosperity, 100 years later. The Negro is still languished in the corners of American society and finds himself an exile in his own land."
text_to_speech3 = "And so we've come here today, To dramatize, a shameful condition. In a sense, we've come to our nation's capital to cash a check.when The Architects of our Republic, Wrote The Magnificent words of the Constitution and the Declaration of Independence. They were signing a promissory note. To which every American was to fall, heir. This note was a promise that all men, yes, black men as well as white men. Would be guaranteed, the unalienable rights of life, liberty and the pursuit of happiness. It is obvious today that America has defaulted on this promissory note insofar as her citizens of color are concerned instead of honoring this sacred obligation. America has given the Negro people, a bad check a check which has come back marked insufficient funds"
text_to_speech4 = "but we refuse to believe that the bank of justice is bankrupt. We refuse to believe that that I insufficient funds in the great vaults of opportunity of this nation. So we've come to cash this. Check a check that will give us upon demand The Riches of freedom and the security of Justice. We have also come to this hallowed spot. To remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real. The promises of democracy. Now is the time to rise from the dark and desolate Valley of segregation to the sunlit path of racial Justice now, is the time To lift our nation from the quicksands of racial Injustice to the solid rock of Brotherhood. Now is the time to make Justice a reality for all of God's children."
text_to_speech5 = "It would be fatal for the nation. To overlook the urgency of the moment. This sweltering, Summer of the negro's legitimate discontent will not pass, until there is an invigorating Autumn of freedom and equality. 1963 is not an end but a beginning, those who hope that the Negro needed to blow off steam. And will now be content will have a rude awakening if the nation returns to business as usual?"
text_to_speech6 = "There will be neither rest nor Tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of Revolt will continue to shake the foundations of our nation until the bright day of Justice emerges. But that is something that I must say to, my people who stand on the warm threshold which leads into the Palace of Justice in the process of gaining our rightful place. We must not be guilty of wrongful Deeds. Let us not seek to Freedom by drinking from the cup of bitterness and hatred. The generate into physical violence against another game. We must rise to the Majestic Heights. Leaving physical force with soul for The Marvelous new militancy 3000 of the Negro Community must not lead us to a distrust of all white people for many of our White Brothers as evidenced by their presence here today."
text_to_speech7 = "We cannot walk alone as we walk. We must make the pledge that we shall always March ahead. We cannot turn back. Now, those were asking the deputies of civil, right? When will you be satisfied? Read the never be satisfied. As long as the Negro is the victim of the Unspeakable horrors of police brutality. We can never be satisfied as long as we can. Not be satisfied as long as the Negro in Mississippi, cannot vote and a negro in New York believes, he has nothing for which to vote. No, we are not satisfied and we will not be satisfied. Until Justice rolls down like Waters and righteousness, like a mighty stream."
text_to_speech8 = "I'm not my unmindful that some of you have come here. Autographed trials and tribulations. Some of you have come fresh from now or a jail sale. Some of you have come from areas where your press Quest. For Freedom left, you battered by the storms of persecution and staggered by The Winds of police brutality. You have been the veterans of creative suffering continue to work with the faith. That on urns suffering is Redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia. Go back to Louisiana, go back to the slums and ghettos of our Northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair. I say to you today, my friend. So even though we Face the difficulties of today and tomorrow, I still have a dream. It is a dream, deeply rooted in the American dream. I have a dream that one day. This nation will rise up live out the true meaning of its Creed. We hold these truths to be self-evident that all men are created equal."
text_to_speech9 = "I have a dream that one day on the Red Hills of Georgia, the sons of former slaves and the sons of former slave owners, will they be able to sit down together at the table of Brotherhood? I have a dream that one day Even the state of Mississippi, a state sweltering with the heat of Injustice, sweltering with the heat of Oppression will be transformed into an oasis of freedom and Justice. I have a dream My four little children will one day live in a nation where they will, not be judged by the color of their skin, but by the content of their character, I have a dream today,"
text_to_speech10 = "I have a dream that one day down In Alabama with its vicious racists with its Governor. Having his lips dripping with the words of interposition and nullification one day right there in Alabama. Little black boys and black girls will be able to join hands with little white boys and white girls as sisters. And brothers, I have a dream today."
text_to_speech11 = "I have a dream that one day, every Valley shall be exalted every Hill and Mountain shall be made low. The rough places will be made plain and the Crooked places will be made straight and the glory of the Lord shall be revealed and All Flesh shall see it together. This is our hope. This is the faith that I go back to the South with, with this faith. We will be able to Hew out of the Mountain of Despair, a stone. Stone of Hope with this faith, we will be able to transform the jangling discords of our nation into a beautiful Symphony of Brotherhood with this faith. We will be able to work together to pray together to struggle together to go to jail together to stand up for Freedom together. Knowing that we will be free one day."
text_to_speech12 = "This will be the day. This will be the day when all of God's children be able to sing with new meaning, my country tis of thee, sweet land of liberty of Thee. I Sing land where my fathers died, land of the Pilgrims Pride from every Mountainside, Let Freedom Ring. And if America is to be a great nation, this must become true."
text_to_speech13 = "So, Let Freedom Ring from the prodigious Cups of New Hampshire. Let Freedom Ring from the mighty mountains of New York. Let Freedom Ring from the heightening alleghenies of Pennsylvania. Let Freedom Ring from the snow-capped Rockies of Colorado. Let Freedom Ring from the curvaceous, slopes of California. But not only that, Let Freedom Ring from Stone Mountain of Georgia. Let Freedom Ring from Lookout Mountain of Tennessee. Let Freedom Ring from every Hill and molehill of Mississippi from every Mountainside. Let Freedom Ring. And when this happens, When we allow freedom to ring, when we let it ring from every village and every Hamlet from every state and every city, we will be able to speed up that day. When all of God's children black men and white, men Jews, and Gentiles Protestants, and Catholics will be able to join hands and sing in the words of the old Negro spiritual free at last free at last. God Almighty. We are free at last."

original_text0 = "I have the pleasure to present to you, Dr. Martin Luther King, Jr."
original_text1 = "I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation."
original_text2 = "Five score years ago, a great American in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves, who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity, but 100 years later, the Negro still is not free. 100 years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. 100 years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. 100 years later, the Negro is still languished in the corners of American society and finds himself in exile in his own land."
original_text3 = "So we've come here today to dramatize the shameful condition. In a sense, we've come to our nation's capital to cash a check. When the architects of our Republic wrote the magnificent words of the Constitution and the Declaration of Independence, they were signing a promissory note to which ever American was to fall heir. This note was a promise that all men, yes, black men as well as white men, would be guaranteed the unalienable rights of life, liberty, and the pursuit of happiness. It is obvious today that America has defaulted on this promissory note in so far as her citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad check, a check which has come back marked insufficient funds."
original_text4 = "But we refuse to believe that the bank of justice is bankrupt. We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation. So we've come to cash this check, a check that will give us upon demand the riches of freedom, and the security of justice. We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quicksands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God's children."
original_text5 = "It would be fatal for the nation to overlook the urgency of the moment. This sweltering summit of the Negroes legitimate discontent will not pass until that is an invigorating autumn of freedom and equality. 1963 is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual."
original_text6 = "There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges. But that is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place, we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred. We must forever conduct our struggle on the high plain of dignity and discipline. We must not allow our creative protests to degenerate into physical violence. Again and again, we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy, which has engulfed the Negro community, must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize their destiny is tied up in our destiny."
original_text7 = "They have come realize that their freedom is inextricably bound to our freedom. We cannot walk alone, and as we walk, we must make the pledge that we shall always march ahead. We cannot turn back. They are those who asking the devotees of civil rights, when will you be satisfied? We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negroes basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating, For Whites Only. We cannot be satisfied as long as a Negro in Mississippi cannot vote, and a Negro in New York believes he has nothing for which to vote. No, we are not satisfied and we will not be satisfied until justice rolls down like waters and righteousness like a mighty stream."
original_text8 = "I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that honor and suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair. I say to you today, my friend, so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream. I have a dream that one day this nation will rise up and live out the true meaning of its creed, 'We hold these truths to be self evident that all men are created equal.'"
original_text9 = "I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day, even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day live in a nation where they will not be judged by the color of our skin, but by the content of that character. I have a dream today."
original_text10 = "I have a dream that one day down in Alabama with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification, one day right there in Alabama, little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers. I have a dream today."
original_text11 = "I have a dream that one day every valley shall be exalted, and every hill and mountain shall be made low, the rough places will be made plain and the crooked places will be made straight and the glory of the Lord shall be revealed and all flesh shall see it together. This is our hope. This is a faith that I go back to the South with. With this faith, we will be able to hew out of the mountain of despair, a stone of hope. With this faith, we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith, we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day."
original_text12 = "This will be the day, this will be the day when all of God's children will be able to sing with new meaning, My country, Tis of thee, Sweet land of Liberty, Of thee I sing. Land where my fathers died, Land of the Pilgrim's pride, From every mountainside, Let freedom ring. If America is to be a great nation, this must become true."
original_text13 = "So let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania. Let freedom ring from the snow capped Rockies of Colorado. Let freedom ring from the curvaceous slopes of California. But not only that, let freedom ring from Stone Mountain of Georgia. Let freedom ring from Lookout Mountain of Tennessee. Let freedom ring from every hill and molehill of Mississippi. From every mountainside, let freedom ring, and when this happens, when we allow freedom ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and gentiles, Protestants and Catholic, will be able to join hands and sing in the words of the old Negro spiritual, Free at last! Free at last! Thank God Almighty, we are free at last!"

diff = difflib.unified_diff(original_text0.split("\n"), text_to_speech0.split("\n"))


def sequenceMatch(text_to_speech0, original_text0):
    matcher = difflib.SequenceMatcher(None, text_to_speech0, original_text0)
    return matcher.ratio()


def matching_blocks(text_to_speech0, original_text0):
    matcher = difflib.SequenceMatcher(None, text_to_speech0, original_text0)
    matching_blocks = matcher.get_matching_blocks()
    # length of the matching blocks
    matching_length = sum(match[2] for match in matching_blocks)
    # length of the longer string
    longer_length = max(len(text_to_speech0), len(original_text0))
    return matching_length / longer_length


def inline_diff(a, b):
    matcher = difflib.SequenceMatcher(None, a, b)

    def process_tag(tag, i1, i2, j1, j2):
        if tag == "replace":
            return "{" + matcher.a[i1:i2] + " -> " + matcher.b[j1:j2] + "}"
        if tag == "delete":
            return "{- " + matcher.a[i1:i2] + "}"
        if tag == "equal":
            return matcher.a[i1:i2]
        if tag == "insert":
            return "{+ " + matcher.b[j1:j2] + "}"
        assert False, "Unknown tag %r" % tag

    return "".join(process_tag(*t) for t in matcher.get_opcodes())


col_header = ["-- TOPIC -- ", "-- VALUE  --"]
df = pd.DataFrame(columns=col_header)
for m in range(14):
    ts_text = eval(f"text_to_speech{m}")
    og_text = eval(f"original_text{m}")
    df.loc[len(df)] = ["PARAGRAPH", m + 1]
    df.loc[len(df)] = ["ORIGINAL", og_text]
    df.loc[len(df)] = ["NLP TEXT TO SPEECH", ts_text]
    df.loc[len(df)] = [
        "INLINE DIFF",
        inline_diff(
            ts_text.upper().translate(str.maketrans("", "", string.punctuation)),
            og_text.upper().translate(str.maketrans("", "", string.punctuation)),
        ),
    ]
    df.loc[len(df)] = [
        "MATCHING BLOCKS",
        matching_blocks(
            ts_text.upper().translate(str.maketrans("", "", string.punctuation)),
            og_text.upper().translate(str.maketrans("", "", string.punctuation)),
        ),
    ]
    df.loc[len(df)] = [
        "SEQUENCE MATCH",
        sequenceMatch(
            ts_text.upper().translate(str.maketrans("", "", string.punctuation)),
            og_text.upper().translate(str.maketrans("", "", string.punctuation)),
        ),
    ]
    df.loc[len(df)] = ["", ""]

# Set the expand_frame_repr and max_colwidth options
pd.set_option("expand_frame_repr", True)
pd.set_option("max_colwidth", 50)
df.to_csv("comparison.csv", index=False)
