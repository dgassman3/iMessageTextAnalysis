# iMessageTextAnalysis
##To get different statistics about iMessage conversations

This is a little project I worked on for my girlfriend to analyze our text conversation over six months.
The end result was some graphs detailing our most frequent words (combined, by person), most frequently texted times, etc.

I used Python to do the word frequency counts, and DB Browser for SQLite for returning pretty much all the other statistics. All the data was imported into Power BI and graphs/visuals were made there.

NOTE -- You will need to locally backup your iPhone to your computer and be able to locate the db file for your text messages. It's a pretty simple process. Once your iPhone is backed up, navigate to:
C:\Users\[YOUR USERNAME]\AppData\Roaming\Apple Computer\MobileSync\Backup\fce7e593a331c39295fa9104a0d6c52697e973a0

The actual file will be named "3d0d7e5fb2ce288813306e4d4636395e047a3d28.mddata."
It will usually be pretty big, mine was 157 MB.

Once you have located this file, you can import that db file into DB Browser (or similar tool).
