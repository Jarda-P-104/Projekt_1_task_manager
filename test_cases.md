# Testovací scénář pro Task manager
    
## Funkce: hlavni_menu()

### TC-01 Volba 1: Přidání nového úkolu  
**Popis:** Ověření, že volba stiskem klávesy čísla 1 v hlavním menu správně spustí funkci 	pridat_ukol()
**Vstupní podmínky:** Program je spuštěn a zobrazuje hlavní menu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program spustí funkci pridat_ukol().
**Skutečný výsledek:** Funkce pridat_ukol() byla spuštěna a program zobrazil výzvu k zadání nového úkolu
**Stav:** PASS
**Poznámky:** Tento případ je důležitý, protože ověřuje základní navigaci z hlavního menu a funkčnost jedné z klíčových funkcí programu.

### TC-02 Volba 2: Zobrazení úkolů  
**Popis:** Ověření, že volba čísla 2 v hlavním menu spustí funkci zobrazit_ukoly().
**Vstupní podmínky:** Program je spuštěn a zobrazuje hlavní menu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 2 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program spustí funkci zobrazit_ukoly().
**Skutečný výsledek:** Program zobrazil seznam úkolů nebo hlášku „Nejsou žádné úkoly“.
**Stav:** PASS
**Poznámky:** Ověření správné navigace.

### TC-03 Volba 3: Odstranění úkolu  
**Popis:** Ověření, že volba čísla 3 správně spustí funkci odstranit_ukol().
**Vstupní podmínky:** Program zobrazuje hlavní menu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu “Nakoupit“ a stiskněte klávesu Enter.
5. Zadejte popis úkolu “Koupit mléko“ a stiskněte klávesu Enter.
6. Zadejte číslo 3 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program zobrazí seznam úkolů a vyzve uživatele k zadání čísla úkolu pro odstranění přes funkci odstranit_ukol()
**Skutečný výsledek:** Program zobrazil seznam úkolů a výzvu k odstranění.
**Stav:** PASS
**Poznámky:** Ověření správného propojení menu s funkcí odstranit_ukol().

### TC-04 Volba 4: Ukončení programu  
**Popis:** Ověření, že volba čísla 4 v hlavním menu ukončí program
**Vstupní podmínky:** Program zobrazuje hlavní menu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 4 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program zobrazí text “Ukončili jste program“ a následně ukončí program.
**Skutečný výsledek:** Program byl ukončen.
**Stav:** PASS
**Poznámky:** Základní pozitivní test pro ukončení programu.
        
### TC-05 Neplatná volba v menu  
**Popis:** Ověření, že po zadání neplatného čísla z menu upozorní program uživatele na neplatnou volbu a zobrazí validní rozsah hodnot. 
**Vstupní podmínky:** Program zobrazuje hlavní menu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 5 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program zobrazí hlášku o neplatné volbě. 
**Skutečný výsledek:** Program zobrazí text “Neplatná hodnota - Zadejte číslo 1-4“ a následně zobrazí celé menu.
**Stav:** PASS
**Poznámky:** Negativní test.

## Funkce: pridat_ukol()
### TC-06 Přidání úkolu s platnými údaji  
**Popis:** Ověření úspěšného vytvoření nového úkolu.
**Vstupní podmínky:** Spuštěný program v terminálu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu – “Nakoupit“ a stiskněte klávesu Enter.
5. Zadejte popis úkolu – “Koupit chleba“ a stiskněte klávesu Enter.
**Očekávaný výsledek:** Úkol bude přidán do seznamu. 
**Skutečný výsledek:** Funkce pridat_ukol() uloží vstupní data od uživatele a uloží jej do seznamu, zobrazí text “Úkol Nakoupit byl přidán“ a zobrazí   menu s další možností volby.
**Stav:** PASS
**Poznámky:** Základní pozitivní scénář.
        
### TC-07 Prázdný název úkolu  
**Popis:** Ověření kontroly povinného pole název.
**Vstupní podmínky:** Spuštěný program v terminálu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu – Stiskněte klávesu Enter bez textu.
**Očekávaný výsledek:** Program upozorní na nevyplněného povinného pole. 
**Skutečný výsledek:** Program zobrazí text “Zadali jste prazdne pole“ a umožní opakovat zadání názvu úkolu.
**Stav:** PASS
**Poznámky:** Negativní scénář.

### TC-08 Prázdný popis úkolu  
**Popis:** Ověření kontroly povinného pole popis.
**Vstupní podmínky:** Spuštěný program v terminálu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Zadejte název úkolu – “Nakoupit“ a stiskněte klávesu Enter.
5. Zadejte popis úkolu – Stiskněte klávesu Enter bez textu.
**Očekávaný výsledek:** Program upozorní na nevyplněného povinného pole. 
**Skutečný výsledek:** Program zobrazí text “Zadali jste prazdne pole“ a umožní opakovat zadání popisu úkolu.
**Stav:** PASS
**Poznámky:** Negativní scénář.

### TC-09 Zadání názvu obsahujícího pouze mezery
**Popis:** Ověření chování aplikace při zadání názvu tvořeného pouze mezerami.
**Vstupní podmínky:** Program čeká na zadání názvu úkolu.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 1 a potvrďte stisknutím klávesy Enter.
4. Na výzvu pro zadání názvu zadejte několik mezer a stiskněte klávesu Enter.
5. Zadejte platný popis úkolu.
**Očekávaný výsledek:** Program by měl vyhodnotit vstup jako neplatný a požadovat zadání platného názvu.
**Skutečný výsledek:** Program přijal název obsahující pouze mezery a vytvořil úkol.
**Stav:** FAIL
**Poznámky:** Nalezená chyba programu. Podmínka while nazev == "" nekontroluje vstupy složené pouze z mezer. Doporučené řešení je použít nazev.strip() == "".

## Funkce: zobrazit_ukoly()

### TC-10 Zobrazení prázdného seznamu úkolů
**Popis:** Ověření správného chování aplikace v případě, že seznam úkolů neobsahuje žádný záznam.
**Vstupní podmínky:** Seznam ukoly je prázdný.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Ověřte, že se zobrazuje hlavní menu s nabídkou voleb (např. "1 - Přidat úkol", "2 - Zobrazit úkoly" atd.).
3. Zadejte číslo 2 a potvrďte stisknutím klávesy Enter.
**Očekávaný výsledek:** Program zobrazí zprávu: “Nejsou žádné úkoly“.
**Skutečný výsledek:** Program zobrazil zprávu „Nejsou žádné úkoly“.
**Stav:** PASS
**Poznámky:** Hraniční případ ověřující správné zpracování prázdného seznamu.

### TC-11 Zobrazení jednoho uloženého úkolu
**Popis:** Ověření, že program správně zobrazí jeden uložený úkol včetně názvu a popisu.
**Vstupní podmínky:** V seznamu ukoly existuje jeden úkol.
**Příklad:**	
Název: Nakoupit
Popis: Koupit mléko
**Kroky testu:**
1. Spusťte program v terminálu
2. Stiskněte klávesu 1
3. Zadejte název úkolu “Nakoupit“ a stiskněte klávesu Enter
4. Zadejte popis úkolu “Koupit mléko“ a stiskněte klávesu Enter
5. Zvolte možnost „2 – Zobrazit všechny úkoly“.
**Očekávaný výsledek:** Program zobrazí seznam úkolů obsahující jeden záznam s číslem 1, názvem a popisem úkolu.
**Skutečný výsledek:** Program zobrazil jeden úkol se správným názvem a popisem.
**Stav:** PASS
**Poznámky:** Pozitivní test ověřující základní funkcionalitu výpisu úkolů.

### TC-12 Zobrazení více úkolů
**Popis:** Ověření, že aplikace zobrazí všechny uložené úkoly a správně je očísluje.
**Vstupní podmínky:** V seznamu ukoly existují alespoň dva úkoly.
**Příklad:**	
Nakoupit – Koupit mléko
Uklidit – Uklidit pokoj
**Kroky testu:**
1. Spusťte program v terminálu
2. Stiskněte klávesu 1
3. Zadejte název úkolu “Nakoupit“ a stiskněte klávesu Enter
4. Zadejte popis úkolu “Koupit mléko“ a stiskněte klávesu Enter
5. Stiskněte klávesu 1
6. Zadejte název úkolu “Uklidit“ a stiskněte klávesu Enter
7. Zadejte popis úkolu “Uklidit pokoj“ a stiskněte klávesu Enter
8. Zvolte možnost „2 – Zobrazit všechny úkoly“.
**Očekávaný výsledek:** Program zobrazí všechny uložené úkoly ve správném pořadí s odpovídajícím číslováním.
**Skutečný výsledek:** Program zobrazil všechny úkoly ve správném pořadí.
**Stav:** PASS
**Poznámky:** Pozitivní test ověřující správné fungování cyklu for a číslování úkolů.

### TC-13 Kontrola přečíslování po odstranění úkolu
**Popis:** Ověření, že po odstranění úkolu aplikace správně přečísluje zbývající položky.
**Vstupní podmínky:** V seznamu existují minimálně tři úkoly.
**Příklad:**	
Úkol A
Úkol B
Úkol C
**Kroky testu:**
1. Spusťte program v terminálu.
2. Stiskněte klávesu 1 a potvrďte klávesou Enter
3. Zadejte název úkolu “Úkol“ a stiskněte klávesu Enter
4. Zadejte popis úkolu “A“ a stiskněte klávesu Enter
5. Stejným způsobem přidejte další dva úkoly.
6. Stiskněte klávesu 3 a stiskněte klávesu Enter
7. Odstraňte druhý úkol.
8. Zvolte možnost stiskem klávesy 2 „Zobrazit všechny úkoly“.
**Očekávaný výsledek:**
    Program zobrazí: 	1 Úkol A
                        2 Úkol C
    Číslování bude navazovat bez mezer.
**Skutečný výsledek:** Program správně přečísloval zbývající úkoly.
**Stav:** PASS
**Poznámky:** Důležitý test ověřující konzistenci výpisu po změně seznamu.

## Funkce: odstranit_ukol()

### TC-14 Odstranění existujícího úkolu
**Popis:** Ověření, že program správně odstraní vybraný úkol ze seznamu.
**Vstupní podmínky:** V seznamu ukoly existuje alespoň jeden úkol.
**Příklad:**	Nakoupit – Koupit mléko
**Kroky testu:**
1. Spusťte program v terminálu.
2. Zvolte stiskem klávesy 1 – přidat nový úkol 
3. Zadejte název úkolu “Nakoupit“
4. Zadejte popis úkolu “Koupit mléko“
5. Zvolte stiskem klávesy 3 – Odstranit úkol
6. Zadejte klávesou číslo 1 a potvrďte klávesou Enter 
**Očekávaný výsledek:** Program odstraní vybraný úkol a zobrazí zprávu: „Úkol Nakoupit byl odstraněn“.
**Skutečný výsledek:** Úkol byl odstraněn a zobrazena potvrzovací zpráva.
**Stav:** PASS
**Poznámky:** Základní pozitivní scénář ověřující hlavní funkcionalitu mazání úkolů.

### TC-15 Zadání čísla mimo rozsah seznamu
**Popis:** Ověření reakce programu na zadání čísla, které neodpovídá žádnému existujícímu úkolu.
**Vstupní podmínky:** V seznamu existuje alespoň jeden úkol.
**Příklad:**	Nakoupit – Koupit mléko
**Kroky testu:**
1. Spusťte program v terminálu.
2. Zvolte stiskem klávesy 1 – přidat nový úkol 
3. Zadejte název úkolu “Nakoupit“
4. Zadejte popis úkolu “Koupit mléko“
5. Zvolte stiskem klávesy 3 – Odstranit úkol
6. Zadejte klávesou číslo 99 a potvrďte klávesou Enter 
**Očekávaný výsledek:** Program zobrazí zprávu: „Neplatné číslo“.
**Skutečný výsledek:** Program zobrazil zprávu „Neplatné číslo“.
**Stav:** PASS
**Poznámky:** Negativní test ověřující validaci rozsahu vstupu.

### TC-16 Pokus o odstranění úkolu z prázdného seznamu
**Popis:** Ověření správného chování programu při pokusu odstranit úkol, pokud žádné úkoly neexistují.
**Vstupní podmínky:** Seznam ukoly je prázdný.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Stiskněte klávesu 3 a potvrďte klávesou Enter.
**Očekávaný výsledek:** Program zobrazí zprávu: „Nejsou žádné úkoly“.
**Skutečný výsledek:** Program zobrazil zprávu „Nejsou žádné úkoly“.
**Stav:** PASS
**Poznámky:** Hraniční případ ověřující práci s prázdným seznamem.

### TC-17 Zadání textu místo čísla při odstranění úkolu
**Popis:** Ověření reakce programu na zadání textu místo číselné hodnoty.
**Vstupní podmínky:** V seznamu existuje alespoň jeden úkol.
**Kroky testu:**
1. Spusťte program v terminálu.
2. Zvolte stiskem klávesy 1 – přidat nový úkol 
3. Zadejte název úkolu “Nakoupit“
4. Zadejte popis úkolu “Koupit mléko“
5. Zvolte stiskem klávesy 3 – Odstranit úkol 
6. Na výzvu pro zadání čísla úkolu zadejte text „abc“ a stiskněte klávesu Enter.
**Očekávaný výsledek:** Program upozorní uživatele na neplatný vstup a umožní pokračovat bez ukončení aplikace.
**Skutečný výsledek:** Program byl ukončen výjimkou ValueError a nebylo možné pokračovat v práci s aplikací.
**Stav:** FAIL
**Poznámky:** Nalezená chyba aplikace. Vstup není ošetřen pomocí try/except

### TC-18 Odstranění posledního úkolu v seznamu
**Popis:** Ověření správného odstranění posledního úkolu a následného vyprázdnění seznamu.
**Vstupní podmínky:** V seznamu existuje právě jeden úkol.
**Příklad:**	Nakoupit – Koupit mléko
**Kroky testu:**
1. Spusťte program v terminálu.
2. Zvolte stiskem klávesy 1 – přidat nový úkol 
3. Zadejte název úkolu “Nakoupit“
4. Zadejte popis úkolu “Koupit mléko“
5. Zvolte stiskem klávesy 3 – Odstranit úkol
6. Zadejte klávesou číslo 1 a potvrďte klávesou Enter
7. Stiskněte klávesu 2 a potvrďte klávesou Enter
**Očekávaný výsledek:** Úkol bude odstraněn a při následném zobrazení seznamu se zobrazí zpráva: „Nejsou žádné úkoly“.
**Skutečný výsledek:** Úkol byl odstraněn a seznam je prázdný.
**Stav:** PASS
**Poznámky:** Hraniční případ ověřující správnou práci aplikace po odstranění posledního záznamu.