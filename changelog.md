************
 Changelog
************
 
2.1.0:
	NEW: Medium levels have been added
	Bug fixes:
		Fixed multiple issues when timing out:
			Spelling error
			Wrong message
		Length of ¬¬¬ being too short

2.0.0:
	NEW: levels, you can now play levels of varying difficulty to challenge yourself! (More details in howToPlay)
		 (Only 2 easy levels are currently available)
	NEW: You can now view this changelog in-game
	Visual changes:
		Reworked welcome menu
		Added placeholder for user data
	Other changes:
		Resetting user data includes level completion

1.9.2 (rev2):
	Added placeholder for Play levels
	Bug fixes:
		(Major Fix) - Mulitple programs clashed causing game to run when it is not meant to.
		Some text was incorrectly displayed.
	Other changes:
		Game is now availiable on linux devices

1.9.1:
	NEW: Two extra lists have been added
	NEW: You can now change your difficulty while playing with your own list.
		 This has a default system where you can select a preferred difficulty for ease of access.
	Bug fixes:
		Stats for your own list were incorrectly displayed


1.9.0:
	NEW: difficulty factor; you now only have a certain amount of time to answer each question or letter.
	NEW: Overall difficulty now changes that length aswell as word length
	Updated howToPlay
	Visual changes:
		Improved the first option menu
		pWords option menu is now cleaner
		Words are now stored in lowercase always and titles are forced capitilised for the first letter per word (like an actual title)
		Changed wording of edit word list option and edit title
		Removed placeholder for user data
		Added placeholder for two new sets to choose
		Added placeholder for difficulty level for your own set
	Bug fixes:
		You could choose options higher than 4/5
		* is red

1.8.1:
	Visual changes:
		Replaced countdown screen with a more efficent one (pWords only at the momment)
		More time delays added
		Added placeholder for user stats
		Added under maintenence tag to option 3 in settings.
	Other changes:
		All inputs are now flushed
		Added text that can only be seen if a bug is there
		Added an actual option to stop deleting user data
	Bug fixes:
		Last bit of text in howToPlay were incorrectly displayed
		Clearing a set and then attempting to play that set result in a crash and other issues
		Fixed message not showing when entering a game with too little words (Very old bug!)

1.8.0:
	NEW: You can now remove specific words from your own list;
	tells you which words were removed in case a word was entered that was not in the list.
	Visual changes:
		Changed colour of words in list.
		Shuffled option menu in pWords
	Bug fixes:
		Fixed issue with how words in list were displayed while adding them
	Other changes:
		Disabled choosing overall difficulty (being balanced and updated soon)
		Must now have at least 2 words in a list to be able to play it

1.7.2:
	NEW: Doubled the amount of hard words
	Balance changes:
		Timeout changes:
			easy = 0.6*
			medium = 0.4*
			hard = 0.2*
			anyWord = 0.4*
			player made = 0.2*
			* = seconds + (based on length of word; longer word = longer time)
			(Balanced setting difficulty accordingly)
	Visual changes:
		Changed colour of option 6 in settings


1.7.1:
	NEW: 2 NEW wordList slots have been added
	NEW: If your word list is unplayable, it now tells you.
	Other changes:
		beta tag removed from mananging or playing your own list.
		* now applies to howToPlay

1.7.0:
	NEW: create your own set of words to play. You can edit this at any time. Currently you can only create one set but this will be changed soon.
	Updated howToPlay following this addition
	Added end session to welcome screen
	Visual changes:
		Changed welcome screen to accomodate new update.
		removed coming soon tag from own list.
		Changed normal mode to presets.
		

1.6.0:
	Balance changes:
		each overall difficulty now changes how many bonus points you get:
		1) Casual (+0.5 seconds*), (-5 points**) unless it is easy difficulty,  if so -3 points instead.
		2) Normal (+0 seconds*), (+0 points**)
		3) Serious (-0.25 seconds*), (+2 points**)
		4) Hardcore (-0.5 seconds*), (+5 points**)
		5) Too far! (-1 seconds*), (+10 points**)
	Other changes:
		Text comes in quicker to stop annoying delays
		Changed how you would exit settings, you now press 6.
	Bug fixes:
		Not being able to select the 5^th setting
	NEW: indepth how to play option has been added

1.5.0 (Full release):
	NEW: settings are finally here!:
		Includes the following:
			1) Toggle input method:
			2) Toggle anyWord:
			3) Toggle overall difficulty
			4) Erase user data
			5) Reset settings to default
	Other changes:
		stats pages are now easier to read
		removed beta tag from main game
		back to difficutly changed to back to welcome screen after a round

1.4.0: (BETA)
	NEW: stats will be displayed at the end of session for the following:
		current session
		previous session
		best session
	Stats include points, accuracy, difficulies attempted.
	Balance changes:
		easy timeout: 2 --> 1.5

1.3.1:
	Changes:
		You can no longer enter invalid lengths of string while answering
	Removed version tag from norm.
	bug fixes:
		Fixed issue with spacing of question and answer after round had ended.



1.3.0:
	Normal mode version 2.0:
		Game reworked: now you have to spell the word letter by letter.
	Revamped game screen for lose/win
	reorded game selection menu
	bug fixes:
		colouring issue with question
	balance changes:
		easy timeout: 3 --> 2 seconds
		hard timeout: 1.5 --> 3 seconds

1.2.1: 
	Added placeholder for new gamemode
	NEWS: reworking the game and new gamemode coming soon!

1.2.0:
	New points system: gain or lose points based on your difficulty and whether you get that quesion correct.
	Balance changes:
		all difficulty excluding 'easy ' difficulty have gained the following nerf:
			question timeout + 0.5 seconds
	Other changes:
		increased banner length by 3 *.

1.1.0:
	New anyWord difficulty has been added, contains 400k+ words of all difficulties
	New medium difficulty
	New hard difficulty 
	New: you can now end the session by typing 'end' when prompted
	Bug fixes:
		pressing 'medium' or 'hard' difficulty would take you to easy difficulty
	Balance changes:
		timeout length of question is now based on your difficulty:
			'easy' = 3 seconds
			'medium' = 2 seconds
			'hard' = 1 second
		'anyWord' = 3.5 seconds

1.0.1:
	Bug fixes:
		Banner displaying wrong text
		Buffer not being flushed
	Placeholder added for anyWord difficulty

1.0.0:
	Alpha version live