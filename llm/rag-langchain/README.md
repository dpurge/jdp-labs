# RAG in LangChain

This is my exercise in retrieval-augmented generation.

I have chosen markdown to be the only document format ingested.

The scripts is using a local `llama3.1` model run in Ollama.

Execute in sequence:

- `ingest.py` to convert documents into vector store
- `chat.py` to talk to the model

## Sample of the conversation

Unfortunately, the quality of the responses is not great.

```txt
Query: What languages are spoken in Poland?
Based on the context, there are several minority languages spoken in Poland, including:

1. Kashubian (spoken by around 500,000 people)
2. Belarusan (spoken by around 250-300,000 people)
3. Polish (the national language of Poland, with no exact number mentioned but considered one of the most widely spoken languages in the world)
4. Other minority languages include Slovak, Armenian, Karate, Tatar, Romani, and others.

Additionally, there are regional varieties of Polish spoken in different parts of Poland, such as "frontier Polish" (polszczyzna kresowa) spoken by around 2 million people on the eastern frontier.

Query: What is the main language spoken in Poland?
The main language spoken in Poland is Polish. It's the official language of the country, and over 36 million native speakers are found within its borders, making up around 93-94% of the population.

Query: Where else in the World is Polish spoken?
According to the text, apart from Poland, Polish is also spoken by large communities abroad. These communities can be found in:

* The United States
* Canada
* South America (especially Brazil and Argentina)
* Great Britain
* France (no specific information provided)

Additionally, there are smaller groups of Polish speakers in other countries, but the text does not specify which ones.

Query: Describe the history of Polish.
The history of Polish can be broadly divided into several periods, each marked by significant events and cultural influences that shaped the language.

**Middle Ages (14th-16th centuries)**

During this period, Polish was heavily influenced by Latin due to the spread of Christianity and the introduction of education. Many Latin loanwords entered the language, especially in fields such as law, politics, and academia. The establishment of monastic schools further solidified the use of Latin.

**Renaissance (16th century)**

The 16th century saw a significant increase in educational opportunities, particularly among the nobility. This led to the development of an educational system and the introduction of new vocabulary from Italian, Latin, and other languages. Notable achievements include:

* Jan Mączyński's Latin-Polish dictionary (1564)
* Łukasz Górnicki's theory of language culture (1566)
* Piotr Statorius' first Polish grammar (1568)

**17th century (Saxon period)**

The 17th century was marked by devastating wars, depopulation, and decline of cities. This had a negative impact on the development of Polish, with many potential cultural achievements hindered by the crisis.

**18th century**

The French influence became significant in Poland during the 18th century, particularly at court due to the presence of French queens. Many new borrowings entered the language, such as:

* Artyleria (artillery)
* Dama (dame)
* Fort (fort)
* Gorset (corset)

**Grammatical changes**

Throughout its history, Polish underwent several grammatical changes, including:

* A change in the articulation of ł from apico-dental to nonsyllabic |w| (16th century)
* Decline of the "raised a" after long a (second quarter of the 18th century)
* Depalatalization of labials word-finally (half 18th century)
* Development of the virile gender (masculine personal) and common suffixes across genders in plural cases (16-17th centuries)

These changes reflect the language's ability to adapt and evolve over time, shaped by various cultural influences and historical events.

Query: Does Polish has any dialects?
Yes, Polish has several regional dialects, which are often referred to as "territorial varieties" or "regional languages". Here are five main territorial varieties:

1. **Wielkopolski** (Great Polish): spoken in the western part of Poland, particularly in the Wielkopolskie and Kujawsko-Pomorskie voivodeships.
2. **Małopolski** (Little Polish): spoken in southern Poland, particularly in the Małopolskie voivodeship.
3. **Silesian**: spoken in southwestern Poland, particularly in the Silesian Voivodeship and parts of Lower Silesia.
4. **Mazovian**: spoken in eastern Poland, particularly in the Masovian Voivodeship.
5. **Kashubian** (recognized as a separate regional language): spoken in Pomerania, particularly in the Puck County.

These dialects have distinct features and variations, but they are all considered to be part of the Polish language.

Query: Describe Polish phonology.
Polish phonology is characterized by a distinct set of features that differentiate it from other Slavic languages. Here are some key aspects of Polish phonology:

1. **Vowel system**: Polish has a relatively simple vowel system, consisting of six monophthong vowels (/i/, /ɨ/, /u/, /e/, /a/, and /o/) and four diphthongs (/ie̯/, /uo̯/, /je̯/, an  nd /jo̯/).
2. **Consonant system**: Polish has a wide range of consonantal sounds, including:
        * Stops: /p/, /t/, /k/, /m/, /n/, and /ŋ/
        * Fricatives: /s/, /z/, /š/, /ž/, /x/, /ʃ/, and /h/
        * Nasals: /m/, /n/, and /ŋ/
        * Liquids: /l/ and /j/
3. **Stress**: Polish words typically have a stressed syllable, which can be indicated by the placement of stress marks (e.g., /pɛr̩ˈsku/).
4. **Vowel reduction**: In unstressed positions, vowels in Polish often undergo reduction, becoming more centralized or reduced to schwa (/ə/).
5. **Nasalization**: Nasal vowels are pronounced with a nasal quality, particularly before certain consonant clusters (e.g., /m/ and /n/).
6. **Lention**: In some dialects, especially in the south and east of Poland, /k/ and /g/ may be pronounced as /ʁ/ or /x/, a phenomenon known as lention.
7. **Fronting and backness**: Polish has a tendency to front certain consonant sounds, such as /k/ becoming /ts/ or /dz/. Conversely, the sound /w/ is often back (as [v] or [ɣ]).
8. **Palatalization**: In some dialects, especially in the north and east of Poland, /k/, /g/, and /x/ may be palatalized before /i/ or /j/.
9. **Syllable structure**: Polish allows for a relatively complex syllable structure, with up to four consonant sounds preceding a vowel (e.g., /strɛˈsku/).

These features contribute to the distinct sound and pronunciation of Polish, which can vary across different dialects and regional varieties.

Query: From which languages loan words where coming into Polish?
Based on the text, it appears that loanwords were entering Polish from various languages, but specifically mentioned are:

* French: The influence of French is mentioned as intensifying in the 18th century, and loanwords such as "artyleria" (artillery), "dama" (dame), "fort" (fort), etc. are cited.
* Local languages spoken on the Polish eastern frontier, particularly Ruthenian and Lithuanian: The text notes that the regional variety of Polish spoken in this area, known as "frontier Polish", has been influenced by these local languages.

However, the text does not provide a comprehensive list of languages from which loanwords are entering Polish. It seems to focus more on the historical and linguistic developments within Poland rather than providing information on language contact and borrowing from external languages.

Query: Describe Polish literature.
Polish literature is a rich and diverse field that has been in existence since the Middle Ages. Here are some key points about its development:

**Medieval Period**

Literary masterpieces, such as "Bogurodzica" (11-14th c.) and "Kazania świętokrzyskie" (14th c.), were written during this period.

**Renaissance and Baroque**

The golden age of Polish literature occurred during the Renaissance and Baroque periods under the last Jagiellonians (Sigismund the Old and Sigismund August). Notable authors include Jan Kochanowski, considered the greatest Slavic poet of his time. However, many poets and writers from this period remained unknown due to Poland's cultural isolation in Europe.

**Enlightenment**

Polish literature flourished again during the Enlightenment with notable authors such as Ignacy Krasicki (poet), Hugo Kołłątaj and Stanisław Staszic (publicists), Franciszek Zabłocki and Julian Ursyn Niemcewicz (comedy writers).

**Romantic Period**

Polish poetry reached its peak in the Romantic period with famous poets like Adam Mickiewicz, Juliusz Słowacki, Zygmunt Krasiński, and Cyprian Kamil Norwid.

**19th Century**

The climax of Polish prose occurred after the January Uprising (1863) with notable authors Eliza Orzeszkowa, Bolesław Prus, Henryk Sienkiewicz (first Nobel Prize laureate), Stefan Żeromski, and Stanisław Reymont.

**20th Century**

In recent years, two Polish poets have received the Nobel Prize: Czesław Miłosz (1911-2004) and Wisława Szymborska (born 1923). Notable 20th-century authors include Stanisław Ignacy Witkiewicz "Witkacy", Bruno Schulz, Witold Gombrowicz, Tadeusz Różewicz, Zbigniew Herbert, Sławomir Mrożek, and Stanisław Barańczak.

**Contribution to European Heritage**

Poland's cultural achievements have been significant in introducing fundamental values of political thought, such as the ideas of republican and federation state, civil rights, and the concept of national liberation movement.

Query: What are the languages that are most similar to Polish?
Based on the text, the languages that are most similar to Polish are:

* Other Slavic languages (although no specific language is mentioned)

However, we can infer from the text that Polish is distinct among other Slavic languages in several features such as:

* Penultimate stress (which is unique to Polish)
* Nasalized vowels
* Abundance of palatal consonants

Therefore, if you're looking for a language similar to Polish, you might consider other Slavic languages such as Czech or Slovak (mentioned as living among Poles in Poland), although the text doesn't provide direct comparison.
```
