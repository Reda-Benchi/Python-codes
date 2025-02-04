from rutenett import Rutenett
from celle import Celle
import random 

def assert_variabler(objekt, forventet_variabler):
    # Sjekker om objektet har de forventede variablene
    for variabel in forventet_variabler:
        assert hasattr(objekt, variabel), f"manglende variabel for {objekt.__class__.__name__}: {variabel}"

def assert_metoder(objekt, forventet_metoder):
    # Sjekker om objektet har de forventede metodene
    for metode in forventet_metoder:
        assert hasattr(objekt, metode), f"manglende metode for {objekt.__class__.__name__}: {metode}"

def assert_type(verdi, forventet_typen, navn):
    # Sjekker om verdien er av forventet type
    assert isinstance(verdi, forventet_typen), f"{navn} er av typen {type(verdi).__name__}, men \
                                                det burde være av typen {forventet_typen.__name__}"

def assert_verdi(verdi, forventet_verdi, navn):
    # Sjekker om verdien er lik den forventede verdien
    assert_type(verdi, type(forventet_verdi), navn)
    assert verdi == forventet_verdi, f"{navn} var {verdi} men det burde være {forventet_verdi}"

# ----- Metodene over er kun hjelpemetoder som bruker inne i testene

def test_konstruktoer_uten_rutenett():
    # Tester konstruktøren til Rutenett-objektet uten å fylle rutenettet med celler
    testRutenett = Rutenett(3, 5)

    assert_variabler(testRutenett, ["_ant_rader", "_ant_kolonner"])
    
    assert_verdi(testRutenett._ant_rader, 3, "Rutenett._ant_rader")
    assert_verdi(testRutenett._ant_kolonner, 5, "Rutenett._ant_kolonner")
    
    print("test_konstruktoer_uten_rutenett() - Alt riktig!")

def test_konstruktoer_med_rutenett():    
    # Tester konstruktøren til Rutenett-objektet og sjekker at rutenettet er riktig opprettet
    testRutenett = Rutenett(3, 5) # Rader, Kolonner
    
    assert_metoder(testRutenett, ["_lag_tom_rad", "_lag_tomt_rutenett"])
    assert_variabler(testRutenett, ["_rutenett"])
    
    assert_type(testRutenett._rutenett, list, "Rutenett._rutenett")
            
    for inne_liste in testRutenett._rutenett:
        assert isinstance(inne_liste, list), f"Rutenett._rutenett burde være en nøstet liste, \
                                            men denne raden var av typen {type(inne_liste).__name__}: {inne_liste}"
        
        assert_verdi(len(inne_liste), 5, "Rutenett._rutenett antall kolonner")  # Lengden av en rad (antall kolonner)
        
        assert all([celle is None for celle in inne_liste]), f"forvented at raden inneholder bare None " \
                                                            f"verdier, funnet: {inne_liste}"
    if len(testRutenett._rutenett) > 1:
        assert testRutenett._rutenett[0] is not testRutenett._rutenett[1], \
                f"Rutenett._rutenett elementer refererer til samme liste (rad)"

    assert_verdi(len(testRutenett._rutenett), 3,  # Antall rader
                 "Rutenett._rutenett antall rader")
    
    print("test_konstruktoer_med_rutenett() - Alt riktig!")

def test_fyll_med_tilfeldige_celler():
    # Tester fylling av rutenettet med tilfeldige celler
    testRutenett = Rutenett(3, 5)
    
    assert_metoder(testRutenett, ["fyll_med_tilfeldige_celler"])
    
    random.seed(1)
    testRutenett.fyll_med_tilfeldige_celler()
    random.seed()
        
    status = set()
    
    for i, inne_liste in enumerate(testRutenett._rutenett):
        for j, celle in enumerate(inne_liste):
            assert_type(celle, Celle, f"celle i _rutenett[{i}][{j}]")
            status.add(celle._status)
            
    assert len(status) != 1, f"Alle celler i rutenettet har _status " \
                             f"{status.pop()}, men det burde være noe " \
                             f"levende og noe død"

    print("test_fyll_med_tilfeldige_celler() - Alt riktig!")

# Flere testmetoder følger her, for eksempel test_hent_celle(), test_tegn_rutenett(), etc.
