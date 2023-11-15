METEOSOURCE = {"malta":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-malta",
               "moldova":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-moldova",
               "montenegro":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-montenegro",
               "netherlands":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-netherlands",
               "macedonia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-republic-of-north-macedonia",
               "norway":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-norway",
               "poland":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-poland",
               "portugal":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-portugal",
               "romania":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-romania",
               "serbia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-serbia",
               "slovakia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-slovakia",
               "slovenia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-slovenia",
               "spain":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-spain",
               "sweden":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-sweden",
               "switzerland":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-switzerland",
               "united-kingdom":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-united-kingdom",
               "croatia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-croatia",
               "cyprus":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-cyprus",
               "czechia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-czechia",
               "denmark":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-denmark",
               "estonia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-estonia",
               "finland":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-finland",
               "france":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-france",
               "germany":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-germany",
               "greece":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-greece",
               "hungary":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-hungary",
               "iceland":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-iceland",
               "ireland":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-ireland",
               "israel":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-israel",
               "italy":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-italy",
               "latvia":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-latvia",
               "lithuania":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-lithuania",
               "luxembourg":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-luxembourg",
               "austria":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-austria",
               "belgium":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-belgium",
               "bosnia-herzegovina":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-bosnia-herzegovina",
               "bulgaria":"https://feeds.meteoalarm.org/feeds/meteoalarm-legacy-atom-bulgaria"}

MODELGPT = "gpt-4-1106-preview"
USERDEFAULTPROMPT = (
        "Please answer the question I asked you immediately, "
        "and if there is a natural disaster in the country I am in, "
        "tell me what I should not do, along with instructions. "
        "My question to you is this:\n"
    )

ds__ = """
<center>
<h3>AI-Supported Warnings & Notification System For Natural Disaster</h3>
<h4>Designed by LUX Space Science & Technology</h4>
</center>
"""

INTERFACEEXAMPLES = [
        "List natural disasters in Denmark",
        "I'm driving around Slettnes Lighthouse, is there a natural disaster happening here?",
        "I'm in Spain, are there any natural disasters I should be careful of?"
    ]

MODELVOICE = "tts-1-hd"
DEFAULTVOICE = "fable"