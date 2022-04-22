from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3


class ActionPozdrav(Action):

    def name(self) -> Text:
        return "action_pozdrav"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ahoj, jsem robot rasa, který ti odpoví na všechny dotazy ohledně SPŠE Plzeň.")

        return []


class ActionRozlouceni(Action):

    def name(self) -> Text:
        return "action_rozlouceni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Měj se hezky, ahoj.")

        return []


class ActionObory(Action):

    def name(self) -> Text:
        return "action_obory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global str
        connection = sqlite3.connect('../Chatbot.db')
        cursor = connection.cursor()
        print("Připojení k databázi bylo v pořádku")
        sql = """SELECT odpoved FROM odpovedi WHERE ucel='obory'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            str = ''.join(x)
        dispatcher.utter_message(text=str)
        cursor.close()
        return []


class ActionKontaktni_udaje(Action):

    def name(self) -> Text:
        return "action_kontaktni_udaje"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Údaje naleznete na daném odkaze: https://www.spseplzen.cz/kontakty/")

        return []


class ActionPrihlaska(Action):

    def name(self) -> Text:
        return "action_prihlaska"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="V prvním kole můžete podat 2 přihlášky a v druhém kole neomezené množství.")

        return []


class ActionPrihlaska_osobni(Action):

    def name(self) -> Text:
        return "action_prihlaska_osobni"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Osobní údaje uchazeče, obor vzdělávání, na který podává přihlášku, údaje o zákonném zástupci uchazeče, podpisy uchazeče a zákonného zástupce. Na druhé straně přihlášky vyplněný prospěch ze základní školy 8. a 1. pol. 9. ročníku. Razítko a podpis oprávněné osoby základní školy.")

        return []


class ActionPrihlaska_odevzdat(Action):

    def name(self) -> Text:
        return "action_prihlaska_odevzdat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Od 01.02. do 01.03 – Každý školní rok ve stejném datu. Viz.https://www.spseplzen.cz/prouchazece/prijimacirizeni/)")

        return []


class ActionPrihlaska_studium(Action):

    def name(self) -> Text:
        return "action_prihlaska_studium"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Podat v termínu přihlášku. Viz.https://www.spseplzen.cz/prouchazece/prijimacirizeni/")

        return []


class ActionPrihlaska_lekar(Action):

    def name(self) -> Text:
        return "action_prihlaska_lekar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ne, nemusíte.")

        return []


class ActionPrihlaska_zpusob(Action):

    def name(self) -> Text:
        return "action_prihlaska_zpusob"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Název, kód zvoleného oboru. Viz.https://www.spseplzen.cz/prouchazece/prijimacirizeni/")

        return []


class ActionPrihlaska_kdo(Action):

    def name(self) -> Text:
        return "action_prihlaska_kdo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Přihlášku ke studiu na SŠ podává uchazeč sám nebo jeho zákonný zástupce. Lze ji doručit osobně či poštou.")

        return []


class ActionPrihlaska_poplatek(Action):

    def name(self) -> Text:
        return "action_prihlaska_poplatek"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ne, neplatí.")

        return []


class ActionPrihlaska_sehnat(Action):

    def name(self) -> Text:
        return "action_prihlaska_sehnat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Na základní škole, na webových stránkách naší školy. Viz.https://www.spseplzen.cz/prouchazece/prijimacirizeni/")

        return []


class ActionPrihlaska_potvrdit(Action):

    def name(self) -> Text:
        return "action_prihlaska_potvrdit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ano.")

        return []


class ActionPrihlaska_elektro(Action):

    def name(self) -> Text:
        return "action_prihlaska_elektro"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Přihlášku lze podat elektronicky jen v případě, že zákonný zástupce uchazeče vlastní datovou schránku jako fyzická osoba.")

        return []


class ActionPrijimaci_zkousky(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Jsou 2.")

        return []


class ActionPrijimaci_zkousky_pozvanka(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_pozvanka"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Nejdéle 14 dní před termínem přijímací zkoušky.")

        return []


class ActionPrijimaci_zkousky_nemuzu(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_nemuzu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Do 3 pracovních dní od termínu přijímací zkoušky doručit škole omluvenku od lékaře. Vykonat přijímací zkoušky v náhradním termínu.")

        return []


class ActionPrijimaci_zkousky_vysledky(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_vysledky"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Termín stanovuje MŠMT.")

        return []


class ActionPrijimaci_zkousky_kdo(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_kdo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Všech žáků 9. tříd ZŠ, kteří si podali přihlášku ke studiu na SŠ, která využívá jednotné přijímací zkoušky CERMAT.")

        return []


class Actionprijimaci_zkousky_predmety(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_predmety"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Z matematiky a českého jazyka a literatury.")

        return []


class ActionPrijimaci_zkousky_skola(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_skola"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ano.")

        return []


class ActionPrijimaci_zkousky_datum(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_datum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Termín přijímacích zkoušek stanovuje MŠMT. Viz.https://www.msmt.cz/vzdelavani/strednivzdelavani/prijimaninastredniskolyakonzervatore")

        return []


class ActionPrijimaci_zkousky_misto(Action):

    def name(self) -> Text:
        return "action_prijimaci_zkousky_misto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Zde: https://www.spseplzen.cz/vysledkyprijimackytest/")

        return []


class ActionPodminky_prijeti(Action):

    def name(self) -> Text:
        return "action_podminky_prijeti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Nejdéle do 31.01 Každý školní rok ve stejném datu.")

        return []


class ActionZapisovy_listek(Action):

    def name(self) -> Text:
        return "action_zapisovy_listek"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Slouží k potvrzení úmyslu uchazeče stát se žákem příslušného oboru vzdělávání v dané škole.")

        return []


class ActionZapisovy_listek_sehnat(Action):

    def name(self) -> Text:
        return "action_zapisovy_listek_sehnat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Zápisový lístek vydává uchazečům základní škola.")

        return []


class ActionZapisovy_listek_pocet(Action):

    def name(self) -> Text:
        return "action_zapisovy_listek_pocet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Podat jen jednou, ale je možné jej na základě přijetí po odvolání vzít zpět a podat na obor, na který je uchazeč přijat po odvolání.")

        return []


class ActionZapisovy_listek_ztrata(Action):

    def name(self) -> Text:
        return "action_zapisovy_listek_ztrata"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Základní škola vydá žákovi nový zápisový lístek.")

        return []


class ActionZapisovy_listek_kdy(Action):

    def name(self) -> Text:
        return "action_zapisovy_listek_kdy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Podat jej musí uchazeč nejdéle do 10 pracovních dní od zveřejnění výsledků v případě přijetí.")

        return []


class ActionNeprijeti(Action):

    def name(self) -> Text:
        return "action_neprijeti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Do 3 pracovních dnů podat odvolání proti nepřijetí.")

        return []


class ActionNeprijeti_zasady(Action):

    def name(self) -> Text:
        return "action_neprijeti_zasady"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Odvolání proti nepřijetí může být vyřízeno kladně jedině na základě uvolnění kapacity obory, tzn. některý z přijatých uchazečů nepodá zápisový lístek.")

        return []


class ActionStudium_na_skole(Action):

    def name(self) -> Text:
        return "action_studium_na_skole"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Zaměření je možno změnit na základě žádosti a po vykonání rozdílových zkoušek.")

        return []


class ActionStudium_na_skole_ubytovani(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_ubytovani"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Součástí VOŠ a SPŠE Plzeň je domov mládeže.")

        return []


class ActionStudium_na_skole_finance(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_finance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Naše škola nemá školné, škola je státní.")

        return []


class ActionStudium_na_skole_dalkovy(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_dalkovy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bohužel ne.")

        return []


class ActionStudium_na_skole_pocet_zaku(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_pocet_zaku"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Na naší škole je momentálně 1075 žáků.")

        return []


class ActionStudium_na_skole_maturity(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_maturity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Úspěšnost u maturit je 86,8 %.")

        return []


class ActionStudium_na_skole_souteze(Action):

    def name(self) -> Text:
        return "action_studium_na_skole_souteze"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ano, mnoho žáků SŠ se zúčastňuje několika soutěží (např. matematická olympiáda, SOČ).")

        return []


class ActionPo_skole(Action):

    def name(self) -> Text:
        return "action_po_skole"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="90 % všech absolventů SŠ pokračuje ve studiu na VŠ, zda jí dokončí, nemáme povědomost.")

        return []


class ActionAdaptacni_kurz(Action):

    def name(self) -> Text:
        return "action_adaptacni_kurz"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Koná se ještě před nástupem do školy.")

        return []


class ActionKontaktni_udaje_reditelka(Action):

    def name(self) -> Text:
        return "action_kontaktni_udaje_reditelka"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Ředitelka školy je Ing. Naděžda Mauleová, MBA.")

        return []


class ActionUspesnost_statnich_maturit(Action):

    def name(self) -> Text:
        return "action_uspesnost_statnich_maturit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Úspěšnost u státních maturit je 96,2%.")

        return []


class ActionSance_na_prijeti(Action):

    def name(self) -> Text:
        return "action_sance_na_prijeti"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Šance je vždy. Nejvíce záleží na výsledcích přijímacích zkoušek.")

        return []
