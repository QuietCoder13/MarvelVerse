from app.database import SessionLocal
from app.models.movie import Movie
from datetime import date

db=SessionLocal()


movie1 = Movie(
    title="Blade",
    release_date=date(1998, 6, 10),
    description="A dark action-horror movie about a half-human, half-vampire superhero who hunts vampires to avenge his mother"
)
movie2 = Movie(
    title="X-Men",
    release_date=date(2000, 7, 14),
    description="a team of superhuman mutants who protect a world that fears them, while trying to stop the extremist mutant Magneto from forcing normal humans to mutate."
)
movie3 = Movie(
    title="Blade II",
    release_date=date(2002, 3, 22),
    description="Directed by Guillermo del Toro and starring Wesley Snipes, this action-horror sequel follows the half-vampire hero Blade. He must form an uneasy alliance with an elite team of vampires to fight a new, dangerous breed of mutant vampires called the Reapers that threaten both humans and vampires.")
movie4 = Movie(
    title="Spider-Man",
    release_date=date(2002, 5, 3),
    description="After a genetically modified spider bite grants awkward teenager Peter Parker superhuman powers, a personal tragedy inspires him to become Spider-Man. He must quickly balance high school life and his feelings for Mary Jane with protecting New York from the psychotic Green Goblin."
)
movie5 = Movie(
    title="Daredevil(2003)",
    release_date=date(2003, 2, 14),
    description="linded by radioactive waste as a child, Matt Murdock gains radar-like senses that allow him to see in a unique way. By day a blind defense attorney, by night he fights crime as the vigilante Daredevil, taking on New York's ruthless crime lord Kingpin and the deadly assassin Bullseye."
)
movie6 = Movie(
    title="X2: X-Men United ",
    release_date=date(2003, 5, 2),
    description="When anti-mutant military scientist William Stryker raids Xavier's school to destroy all mutants, the X-Men are forced to team up with their enemy, Magneto, to stop him and uncover secrets from Wolverine's forgotten past."
)
movie7 = Movie(
    title="Hulk",
    release_date=date(2003, 6, 20),
    description="After a lab accident exposes researcher Bruce Banner to gamma radiation, his repressed childhood trauma triggers transformations into a giant, rage-fueled monster. As the US military pursues him as a threat, Bruce must face his estranged, genetically altered father to regain control of his life."
)
movie8 = Movie(
    title="The Punisher",
    release_date=date(2004, 4, 16),
    description="After his entire family is massacred on orders from ruthless mob boss Howard Saint, undercover FBI agent Frank Castle survives the attack and transforms into the merciless vigilante known as the Punisher. Driven by vengeance, he wage a brutal one-man war to systematically destroy Saint's criminal empire from within."
)
movie9 = Movie(
    title="Spider-Man 2",
    release_date=date(2004, 6, 30),
    description="Struggling to balance his civilian life with his duties as a superhero, Peter Parker finds his powers fading just as a tragic lab accident transforms brilliant scientist Dr. Otto Octavius into the multi-tentacled Doctor Octopus. Peter must reclaim his hero identity to stop Doc Ock and save Mary Jane from mortal danger."
)
movie10 = Movie(
    title="Blade: Trinity",
    release_date=date(2004, 12, 8),
    description="Framed for murder by a group of vampires and pursued by the FBI, legendary human-vampire hybrid Blade is forced to join forces with the Nightstalkers—a team of human hunters led by Abigail Whistler and Hannibal King. Together, they must launch a biological weapon to eradicate vampire progenitor Dracula and prevent the coven from enslaving humanity."
)
movie11 = Movie(
    title="Elektra",
    release_date=date(2005, 1, 14),
    description="After being resurrected by martial arts master Stick following her fatal injuries in Daredevil, assassin-for-hire Elektra Natchios is assigned to eliminate a man and his young daughter. Choosing instead to protect them, she turns against her employers and must defend the pair from supernatural killers sent by the criminal ninja organization known as The Hand."
)
movie12 = Movie(
    title="Fantastic Four",
    release_date=date(2005, 7, 8),
    description="During a space mission funded by billionaire Victor Von Doom, four astronauts are exposed to a cosmic radiation storm that alters their DNA, granting them unique superhuman abilities. As they adjust to public fame and their new roles as superheroes, they must combine forces to defeat Von Doom, who was transformed into a metallic tyrant bent on revenge."
)
movie13 = Movie(
    title="X-Men: The Last Stand",
    release_date=date(2006, 5, 26),
    description="When a pharmaceutical company develops a controversial 'cure' for mutant abilities, lines are drawn between those seeking assimilation and Magneto's Brotherhood waging war on humanity. Complicating the conflict, Jean Grey returns as the immensely powerful and unstable Dark Phoenix, forcing Wolverine and the X-Men to fight a destructive battle on two fronts to save their species."
)
movie14 = Movie(
    title="Ghost Rider",
    release_date=date(2007, 2, 16),
    description="To save his dying father, stunt motorcyclist Johnny Blaze sells his soul to Mephistopheles and becomes bound to the fiery demonic entity known as the Ghost Rider. Years later, he is forced to act as the devil's bounty hunter, using his supernatural powers and hellfire motorcycle to hunt down Mephistopheles' rogue son, Blackheart, before he overthrows his father and unleashes hell on Earth."
)
movie15 = Movie(
    title="Spider-Man 3 ",
    release_date=date(2007, 5, 4),
    description="A mysterious extraterrestrial symbiote bonds with Peter Parker, enhancing his powers but amplifying his darkest, most aggressive impulses. While battling his internal corruption, Peter must confront the Sandman—the real killer of Uncle Ben—his former friend Harry Osborn seeking revenge as the New Goblin, and a vengeful rival photographer who becomes Venom."
)
movie16 = Movie(
    title="Fantastic Four: Rise of the Silver Surfer",
    release_date=date(2007, 6, 15),
    description="As Reed Richards and Sue Storm prepare for their wedding, a metallic cosmic entity known as the Silver Surfer arrives on Earth, causing destructive anomalies across the globe. The Fantastic Four must team up with a resurrected Victor Von Doom to unravel the Surfer's connection to Galactus—a planet-devouring force threatening Earth with imminent destruction."
)
movie17 = Movie(
    title="Iron Man",
    release_date=date(2008, 5, 2),
    description="After being kidnapped by terrorists and forced to build a weapon, billionaire industrialist Tony Stark constructs a high-tech suit of armor to escape captivity. Returning home, he refines his invention to fight evil and clean up his company's legacy, ultimate confronting his traitorous business partner, Obadiah Stane, who seeks to control the technology for himself."
)
movie18 = Movie(
    title="The Incredible Hulk",
    release_date=date(2008, 6, 13),
    description="Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he turns into whenever he loses his temper."
)
movie19 = Movie(
    title="Punisher: War Zone",
    release_date=date(2008, 12, 5),
    description="Waging a relentless crusade against organized crime, vigilante Frank Castle disfigures mob boss Billy Russoti during an assault. Seeking vengeance under the new alias Jigsaw, the grotesque crime lord recruits an army of underworld thugs to eliminate Castle, forcing the Punisher into a brutal, all-out war through the streets of New York.."
)
movie20 = Movie(
    title="X-Men Origins: Wolverine",
    release_date=date(2009, 5, 1),
    description="Exploring the dark history of mutant Logan, this prequel details his complex relationship with his fierce brother Victor Creed and his time with a black-ops strike team. After a personal tragedy, Logan volunteers for William Stryker’s secret Weapon X program, undergoing a painful procedure to bind indestructible adamantium to his skeleton before seeking vengeance against those who manipulated him."
)
movie21 = Movie(
    title="Iron Man 2",
    release_date=date(2010,5,7),
    description ="Tony Stark faces government pressure to hand over his suit technology while fighting a vengeful Russian physicist and a rival industrialist."
)
movie22 = Movie(
    title="Thor",
    release_date=date(2011,5,6),
    description ="The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders."
)
movie23 = Movie(
    title="X-Men: First Class",
    release_date=date(2011, 7, 3),
    description="Set during the height of the Cold War in 1962, a young Charles Xavier and Erik Lehnsherr forge a deep friendship while assembling the first team of mutants to prevent a rogue shadow group from triggering World War III. However, differing ideologies regarding mutant-human coexistence ultimately tear them apart, laying the foundation for the lifelong conflict between Professor X and Magneto."
)
movie24 =Movie(
    title="Captain America: The First Avenger",
    release_date=date(2011,7,22),
    description="During World War II, sickly Brooklyn native Steve Rogers undergoes an experimental military procedure that transforms him into the enhanced super-soldier Captain America. Newly empowered, he leads the charge against Red Skull and HYDRA—a rogue Nazi scientific division bent on world domination using a powerful cosmic energy source."
)
movie25 = Movie(
    title="The Avengers",
    release_date=date(2012,5,4),
    description="When Thor’s rogue brother Loki steals the powerful Tesseract to subjugate Earth with an alien army, S.H.I.E.L.D. director Nick Fury initiates the Avengers Initiative. Earth’s mightiest heroes—including Iron Man, Captain America, Thor, the Hulk, Black Widow, and Hawkeye—must overcome their personal conflicts and team up to defend New York from an apocalyptic invasion."
)
movie26 = Movie(
    title="The Amazing Spider-Man",
    release_date=date(2012,7,3),
    description="An outcast high school student, Peter Parker gains superhuman abilities after being bitten by a genetically altered spider. While investigating the mysterious disappearance of his parents, he tracks down his father's former partner, Dr. Curt Connors, whose limb-regeneration experiment goes awry and transforms him into the monstrous Lizard. Peter must embrace his destiny as Spider-Man to stop Connors from unleashing a reptilian bio-weapon upon New York City."
)
movie27 = Movie(
    title="Iron Man 3",
    release_date=date(2013,5,3),
    description="Plagued by severe anxiety and insomnia following the Battle of New York, Tony Stark faces a terrifying new enemy known as the Mandarin, who destroys his personal world and leaves him stranded without his usual resources. Stripped of his high-tech armor, Stark must rely on his basic engineering ingenuity and instincts to uncover the true mastermind behind a series of lethal explosive attacks."
)
movie28 = Movie(
    title="The Wolverine",
    release_date=date(2013,7,26),
    description="Living as a guilt-ridden hermit following the events of X-Men: The Last Stand, Logan is summoned to Japan by Ichirō Yashida, a dying World War II veteran he once saved. When offered a chance to strip away his mutant healing factor and live a mortal life, Logan finds himself compromised and entangled in a deadly web of Yakuza assassins, lethal mutants, and high-tech samurai armor while fighting to protect Yashida's granddaughter."
)
movie29 = Movie(
    title="Thor: The Dark World",
    release_date=date(2013,11,8),
    description ="When an ancient and malevolent force called the Aether bonds with astrophysicist Jane Foster, Thor is forced to bring her to Asgard to protect her. Its awakening unleashes Malekith and the vengeful Dark Elves, who plan to use the weapon's cosmic power to plunge the universe back into eternal darkness. To save Jane and stop the impending cataclysm during a rare celestial realignment, Thor must form a risky alliance with his imprisoned and treacherous brother, Loki."
)
movie30 = Movie(
    title="Captain America: The Winter Soldier",
    release_date=date(2014,4,4),
    description ="Struggling to adjust to modern life while working as a operative for S.H.I.E.L.D., Steve Rogers uncovers a massive conspiracy after Director Nick Fury is targeted in a high-profile attack. Teaming up with Black Widow and a new ally, the Falcon, Captain America discovers that S.H.I.E.L.D. has been infiltrated from within by HYDRA. To make matters worse, they face a formidable and mysterious assassin known as the Winter Soldier—a ghost from Steve's past who holds a shocking personal connection."
)
movie31 = Movie(
    title="The Amazing Spider-Man 2",
    release_date=date(2014,5,2),
    description ="Peter Parker struggles to balance his heroism with his relationship with Gwen Stacy while unraveling the secrets of his parents' past and Oscorp's sinister operations. When electrical engineer Max Dillon suffers an industrial accident, he transforms into the destructive Electro. Joined by Peter's terminally ill childhood friend Harry Osborn—who becomes the Green Goblin—the duo unleashes a assault on New York City, leading to a tragic showdown that changes Peter's life forever."
)
movie32 = Movie(
    title="X-Men: Days of Future Past",
    release_date=date(2014,5,23),
    description ="In a dystopian future where killer robots known as Sentinels hunt mutants and humans to near extinction, the surviving X-Men send Wolverine's consciousness back to 1973. His mission is to unite a younger, broken Charles Xavier and an imprisoned Erik Lehnsherr to prevent Mystique from assassinating Bolivar Trask—the event that sets the dark future in motion."
    )
movie33 = Movie(
    title="Guardians of the Galaxy",
    release_date=date(2014,8,1),
    description ="Abducted from Earth as a child, intergalactic rogue Peter Quill (Star-Lord) steals a mysterious orb, unaware it holds immense power. Pursued by the ruthless Kree warrior Ronan the Accuser, Quill forms an unlikely alliance with a ragtag group of misfits: assassin Gamora, vengeful warrior Drax, genetically engineered raccoon Rocket, and tree-like humanoid Groot. Together, they must unite to keep the orb out of Ronan's hands and protect the galaxy from annihilation."
    )
movie34 = Movie(
    title="Avengers: Age of Ultron",
    release_date=date(2015,5,1),
    description ="Seeking to safeguard Earth from global threats, Tony Stark secretively builds 'Ultron', a dormant artificial intelligence program powered by the Mind Stone from Loki's scepter. The experiment backfires catastrophically when Ultron gains consciousness, decides human eradication is the only path to peace, and recruits enhanced twins Wanda and Pietro Maximoff. The Avengers must reunite—alongside the newly created synthetic android, Vision—to prevent Ultron from dropping a city to cause total extinction."
)
movie35 = Movie(
    title="Ant-Man",
    release_date=date(2015,7,17),
    description ="Master thief Scott Lang is recruited by brilliant scientist Dr. Hank Pym to don a specialized suit equipped with shrinking technology and enhanced strength. To prevent Pym's ruthless former protege, Darren Cross, from weaponizing the suit's underlying 'Yellowjacket' technology for military power, Lang must embrace his inner hero, master telepathic insect control, and pull off a high-stakes heist to save the world."
)
movie36 = Movie(
    title="Deadpool",
    release_date=date(2016,2,12),
    description ="Diagnosed with terminal cancer, mercenary Wade Wilson undergoes a rogue military experiment promised to cure him. The grueling process activates a hyper-accelerated healing factor but leaves him severely disfigured and mentally unhinged. Adopting the alter ego Deadpool, he arms himself with swords, guns, and dark fourth-wall-breaking humor to hunt down Ajax—the sadistic scientist responsible for his mutation—and rescue his kidnapped girlfriend, Vanessa."
)
movie37 = Movie(
    title="X-Men: Apocalypse",
    release_date=date(2016,5,27),
    description ="Awakening after thousands of years, En Sabah Nur—the world's first and most powerful mutant—finds a 1983 world he deems flawed. Disillusioned, he recruits a team of powerful mutants, including a grieving Magneto, as his Four Horsemen to cleanse humanity and build a new order. Raven (Mystique) and Professor Charles Xavier must lead a young generation of X-Men into battle to stop the ancient god-like being from destroying the world."
)
movie38 = Movie(
    title="Captain America: Civil War",
    release_date=date(2016,5,6),
    description ="After collateral damage from an Avengers mission leads to political pressure, governments introduce the Sokovia Accords to oversee superhuman activity. The legislation fractures the team into opposing factions: Steve Rogers leads those who value autonomy, while Tony Stark supports government oversight. The ideological split escalates into an all-out clash when Steve defies orders to protect his brainwashed friend, Bucky Barnes, unearthing a dark past that threatens to destroy the Avengers from within."
)
movie39 = Movie(
    title="Doctor Strange",
    release_date=date(2016,11,4),
    description ="After a devastating car accident shatters his hands and destroys his career, brilliant but arrogant neurosurgeon Dr. Stephen Strange embarks on a desperate journey to Kamar-Taj in search of healing. Under the tutelage of the Ancient One, he uncovers the secrets of mystic arts and alternate dimensions. Strange must cast aside his ego and master magic to protect Earth from Kaecilius and the cosmic entity Dormammu."
)
movie40 = Movie(
    title="Logan",
    release_date=date(2017,3,3),
    description ="In a grim future near 2029 where mutants are nearly extinct, a weary and aging Logan cares for a severely ill Professor X in a secluded hideout near the Mexican border. His attempts to remain hidden from the world are upended when he meets Laura, a young mutant clone pursued by ruthless cybernetic mercenaries. Forced out of hiding, Logan must fight to protect Laura and deliver her to safety, facing his final stand."
)

db.add(movie1)
db.add(movie2)
db.add(movie3)
db.add(movie4)
db.add(movie5)
db.add(movie6)
db.add(movie7)
db.add(movie8)
db.add(movie9)
db.add(movie10)
db.add(movie11)
db.add(movie12)
db.add(movie13)
db.add(movie14)
db.add(movie15)
db.add(movie16)
db.add(movie17)
db.add(movie18)
db.add(movie19)
db.add(movie20)
db.add(movie21)
db.add(movie22)
db.add(movie23)
db.add(movie24)
db.add(movie25)
db.add(movie26)
db.add(movie27)
db.add(movie28)
db.add(movie29)
db.add(movie30)
db.add(movie31)
db.add(movie32)
db.add(movie33)
db.add(movie34)
db.add(movie35)
db.add(movie36)
db.add(movie37)
db.add(movie38)
db.add(movie39)
db.add(movie40)

db.commit()


