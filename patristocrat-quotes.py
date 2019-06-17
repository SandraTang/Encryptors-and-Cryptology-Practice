#Patristocrat Quotes Practice Game (English)
#by Sandra Tang

from random import randint

#intro
print "Patristocrat Quotes Practice Game (English)"

quotes = [r"""The greatest glory into living lies not into never falling, but into rising every time we fall.""",r"""It always seems impossible until it's done.""",r"""Education is the most powerful weapon which you can use to change the world.""",r"""There is no passion to be found playing small - into settling for a life that is less than the one you are capable of living.""",r"""I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.""",r"""A good head and a good heart are always a formidable combination.""",r"""For to be free is not merely to cast off one's chains, but to live into a way that respects and enhances the freedom of others.""",r"""The greatest glory into living lies not into never falling, but into rising every time we fall.""",r"""And as we let our own light shine, we unconsciously give other people permission to do the same""",r"""After climbing a great hill, one only finds that there are many more hills to climb.""",r"""If you talk to a man into a language he understands, that goes to his head. If you talk to him into his language, that goes to his heart.""",r"""The way to get started is to quit talking and begin doing.""",r"""Anybody can make history. Only a great man can write it.""",r"""Human history into essence is the history of ideas. """,r"""People are trapped into history and history is trapped into them. """,r"""I can’t change history, I don’t want to change history. I can only change the future. I’m working on that. """,r"""Neither the life of an individual nor the history of a society can be understood without understanding both. """,r"""Be honest. We have the science, the technology, and the wealth. What we don’t have is the will, and that’s not a reason that history will accept. """,r"""History has demonstrated that the most notable winners usually encountered heartbreaking obstacles before they triumphed. They won because they refused to become discouraged by their defeats.""",r"""I believe that we must maintain pride into the knowledge that the actions we take, based on our own decisions and choices as individuals, link directly to the magnificent challenge of transforming human history. """,r"""I do not speak Hebrew, but I understand that it has no word for ‘history.’ The closest word for it is memory. """,r"""The best prophet of the future is the past. """,r"""Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.""",r"""Associate yourself with men of good quality if you esteem your own reputation; for 'tis better to be alone than into bad company.""",r"""To be good, and to do good, is all we have to do.""",r"""Nothing can stop the man with the right mental attitude from achieving his goal; nothing on earth can help the man with the wrong mental attitude.""",r"""If your actions inspire others to dream more, learn more, do more and become more, you are a leader""",r"""If life were predictable it would cease to be life, and be without flavor.""",r"""If you look at what you have into life, you'll always have more. If you look at what you don't have into life, you'll never have enough.""",r"""If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.""",r"""Life is what happens when you're busy making other plans.""",r"""Fellow citizens, we cannot escape history. """,r"""Thank you for coming. We’re gonna make some history together today. """,r"""The man who has no sense of history, is like a man who has no ears or eyes. """,r"""Poetry is finer and more philosophical than history; for poetry expresses the universal, and history only the particular. """,r"""After making a mistake or suffering a misfortune, the man of genius always gets back on his feet. """,r"""Soldiers, if there is one among you who wants to kill his general, his Emperor, here I am.""",r"""History is a set of lies agreed upon. """,r"""We learn from history that we don’t learn from history! """,r"""The Revolution introduced me to art, and into turn, art introduced me to the Revolution! """,r"""History is merely gossip. """,r"""Condemn me, it does not matter, history will absolve me. """,r"""History shows that there are no invincible armies. """,r"""Revolutions are the locomotives of history. """,r"""History repeats itself, first as tragedy, second as farce. """,r"""History is a people’s memory, and without a memory, man is demoted to the lower animals. """,r"""Friends, I shall ask you to be as quiet as possible. I don’t know whether you fully understand that I have just been shot; but it takes more than that to kill a Bull Moose. """,r"""When I was a child my mother said to me, ‘If you become a soldier, you’ll be a general. If you become a monk, you’ll be the Pope.’ Instead I became a painter and wound up as Picasso. """,r"""History will have to record that the greatest tragedy of this period of social transition was not the strident clamor of the bad people, but the appalling silence of the good people. """,r"""We are not makers of history. We are made by history. """,r"""I won’t predict anything historic. But nothing is impossible. """,r"""Black history is American history. """,r"""You’re going to relegate my history to a month. """,r"""I don’t believe into accidents. There are only encounters into history. """,r"""There is properly no history; only biography. """,r"""Do not go where the path may lead, go instead where there is no path and leave a trail.""",r"""Life is a succession of lessons which must be lived to be understood.""",r"""To me, this is about preserving history and making it available to everyone. """,r"""History is a pack of lies we play on the dead. """,r"""Indeed, history is nothing more than a tableau of crimes and misfortunes. """,r"""History is mostly guessing; the rest is prejudice. """,r"""Spread love everywhere you go. Let no one ever come to you without leaving happier.""",r"""When you reach the end of your rope, tie a knot into it and hang on.""",r"""Always remember that you are absolutely unique. Just like everyone else.""",r"""Don't judge each day by the harvest you reap but by the seeds that you plant.""",r"""The future belongs to those who believe into the beauty of their dreams.""",r"""Tell me and I forget. Teach me and I remember. Involve me and I learn.""",r"""The best and most beautiful things into the world cannot be seen or even touched - they must be felt with the heart.""",r"""It is during our darkest moments that we must focus to see the light.""",r"""Whoever is happy will make others happy too."""r"""At the end, it's not the years into your life that count. It's the life into your years.""",r"""Never let the fear of striking out keep you from playing the game.""",r"""Life is either a daring adventure or nothing at all.""",r"""Many of life's failures are people who did not realize how close they were to success when they gave up.""",r"""You have brains into your head. You have feet into your shoes. You can steer yourself any direction you choose.""",r"""An unexamined life is not worth living.""",r"""True knowledge exists into knowing that you know nothing.""",r"""When the debate is over, slander becomes the tool of the loser.""",r"""Beware the barrenness of a busy life.""",r"""Education is the kindling of a flame, not the filling of a vessel.""",r"""By all means marry: if you get a good wife, you’ll become happy; if you get a bad one, you’ll become a philosopher.""",r"""To find yourself, think for yourself.""",r"""I cannot teach anybody anything, I can only make them think.""",r"""There is only one good, knowledge, and one evil, ignorance.""",r"""The only good is knowledge and the only evil is ignorance.""",r"""Love is a serious mental disease.""",r"""Wise men talk because they have something to say; fools, because they have to say something.""",r"""Be kind, for everyone you meet is fighting a hard battle.""",r"""Your silence gives consent.""",r"""Music is a moral law. It gives soul to the universe, wings to the mind, flight to the imagination, and charm and gaiety to life and to everything.""",r"""One of the penalties for refusing to participate into politics is that you end up being governed by your inferiors.""",r"""Only the dead have seen the end of war.""",r"""We can easily forgive a child who is afraid of the dark; the real tragedy of life is when men are afraid of the light.""",r"""Man - a being into search of meaning.""",r"""At the touch of love everyone becomes a poet.""",r"""We are what we repeatedly do. Excellence, then, is not an act, but a habit.""",r"""The whole is more than the sum of its parts.""",r"""It is the mark of an educated mind to be able to entertain a thought without accepting it.""",r"""The end of labor is to gain leisure.""",r"""Quality is not an act, it is a habit.""",r"""Educating the mind without educating the heart is no education at all.""",r"""What is a friend? A single soul dwelling into two bodies.""",r"""The roots of education are bitter, but the fruit is sweet.""",r"""Pleasure into the job puts perfection into the work.""",r"""Happiness depends upon ourselves.""",r"""There is geometry into the humming of the strings, there is music into the spacing of the spheres.""",r"""Friends are as companions on a journey, who ought to aid each other to persevere into the road to a happier life.""",r"""Silence is better than unmeaning words.""",r"""Do not say a little into many words but a great deal into a few.""",r"""No one is free who has not obtained the empire of himself.""",r"""Rest satisfied with doing well, and leave others to talk of you as they please.""",r"""Concern should drive us into action and not into a depression. No man is free who cannot control himself.""",r"""Above the cloud with its shadow is the star with its light. Above all things reverence thyself.""",r"""Above all things, reverence yourself.""",r"""The oldest, shortest words — "yes" and "no" — are those which require the most thought.""",r"""No guts, no story. Chris Brady""",r"""My life is my message. Mahatma Gandhi""",r"""Screw it, let’s do it. Richard Branson""",r"""Boldness be my friend. William Shakespeare""",r"""Keep going. Be all in. Bryan Hutchinson""",r"""My life is my argument. Albert Schweitzer""",r"""Dream big. Pray bigger.""",r"""Leave no stone unturned. Euripides""",r"""Fight till the last gasp. William Shakespeare""",r"""Stay hungry. Stay foolish. Steve Jobs Click to tweet""",r"""Broken crayons still color. Click to tweet""",r"""If you want it, work for it.""",r"""You can if you think you can. George Reeves""",r"""Whatever you are, be a good one. Abraham Lincoln""",r"""Impossible is for the unwilling. John Keats""",r"""Grow through what you go through.""",r"""The wisest mind has something yet to learn. George Santanaya""",r"""The past does not equal the future. Tony Robbins""",r"""Good things happen to those who hustle. """,r"""If it matters to you, you’ll find a way. Charlie Gilkey""",r"""Forget about style; worry about results. Bobby Orr""",r"""Whatever you do, do with all your might. Marcus Tullius Cicero""",r"""Dream without fear. Love without limits.""",r"""Every noble work is at first impossible. Thomas Carlyle""",r"""If you’re going through hell, keep going. Winston Churchill""",r"""We are twice armed if we fight with faith. Plato""",r"""Open your mind. Get up off the couch. Move. Anthony Bourdain""",r"""Be faithful to that which exists within yourself. """,r"""Persistence guarantees that results are inevitable. Paramahansa Yogananda""",r"""In life you need either inspiration or desperation. Tony Robbins""",r"""I would rather die on my feet than live on my knees. Euripides""",r"""The true success is the person who invented himself. Al Goldstein""",r"""Let him that would move the world first move himself. Socrates""",r"""Go forth on your path, as it exists only through your walking. Augustine of Hippo""",r"""We can do anything we want to if we stick to it long enough. Helen Keller""",r"""It does not matter how slowly you go as long as you do not stop. Confucius""",r"""Life is fragile. We’re not guaranteed a tomorrow so give it everything you’ve got. Tim Cook""",r"""The two most important days into your life are the day you are born and they day you find out why. Mark Twain""",r"""Never let the fear of striking out keep you from playing the game.""",r"""Life is never fair, and perhaps it is a good thing for most of us that it is not.""",r"""The only impossible journey is the one you never begin.""",r"""In this life we cannot do great things. We can only do small things with great love.""",r"""Only a life lived for others is a life worthwhile.""",r"""The purpose of our lives is to be happy.""",r"""Life is what happens when you're busy making other plans.""",r"""You only live once, but if you do it right, once is enough.""",r"""Live into the sunshine, swim the sea, drink the wild air.""",r"""Go confidently into the direction of your dreams! Live the life you've imagined."""]

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

phrase_length = randint(7, 10)
phrase = ""

phrase = quotes[randint(0, len(quotes)-1)].upper()

#phrase is built now

#now create a new alphabet
#a throw-away array
holder = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#blank array to fill in with letters from the throwaway
correlation = []

#fill in
for j in range(0,26):
  correlation.insert(randint(0, len(correlation)), holder[0])
  holder.pop(0)

#remove hashtag from this to make it print the answer above (for testing purposes)
#print phrase

encrypted_array = []
a = 0
for b in phrase:
  if b in alphabet:
    encrypted_array.append(correlation[alphabet.index(b)])
  a += 1

a = 0
encrypted = ""
for c in encrypted_array:
  encrypted = encrypted + c
  a += 1

print "Guess the original statement! This is the encrypted code:"
print encrypted

#guessing time

guess = ""

while not guess.upper() == phrase:
  guess = raw_input("Your encryption: ")

print "You did it! The encrypted message is %s" % phrase
