# Förberedelseuppgifter

## Uppgift 1

### Rayleighfördelad S.V X

### a)

#### Bestäm ML-skattningen av b

ML skattningen av b blir sqrt(sum\[i = 1 -> n\](xi^2) / (2 \* n))

### b)

#### Bestäm MK-skattningen av b

MK skattningen av b blir sum\[i = 1 -> n\](xi) / n \* sqrt(2 / pi)

## Uppgift 2

#### Hur kan man ta fram ett approximativt konfidensintervall för b? Motivera rimligheten bakom approximationen.

För stora n kan summan av S.V:er enlig gränsvärdessatsen approximeras som normalfördelade
Om vi antar att n är tillräckligt stort för att detta ska gälla blir ju b\*obs (observerade värden på b) utfall från en normalfördelad S.V b\*.
b\* är ju medelvärdet(**X**) \* sqrt(2/pi) (samma som MK-skattningen men stora X)
Då blir problemet att hitta fördelningen för b\*. Väntevärdet får vi från observerade värden, medelvärdet(x) \* sqrt(2/pi) men standardavvikelsen är klurigare.  
Om vi sätter D\[b\*\] = sqrt(V\[b\*\]) är ju V\[b\*\] samma som V\[medelvärdet(**X**) \* sqrt(2/pi) \]
Om vi flyttar ut sqrt(2/pi) får vi ju 2/pi \* V\[medelvärdet(**X**)\], vilket är 2 / (pi \* n) \* V\[X\]  
V\[X\] Kan beräknas som E\[X^2\] - E\[X\]^2 = 2 \* b^2 - pi / 2 \* b^2  (där b beräknas med b\*obs)
=> Standardavvikelsen är då sqrt(2 / (pi \* n) \* b^2 \* (2 - pi / 2)) = d\*obs  
Intervallet bli då Ib = b\*obs +- lambda(a/2) \* d\*obs

## Uppgift 3

## Hur kan man skatta wk = log(yk) = B0 + B1\*xk + ek?

Genom att MK skatta sum((log(yk)-(B0 + B1\*xk))^2) alltså minimera felet kan man få fram en skattning av B0 och B1.

Felet blir normalfördelat för stora N, med väntevärde 0 (om det minimerats) och standardavvikelsen kan skattas som:

s = sqrt(Q0/(n-2))

# Problem

# Problem 1

Okänt väntevärde, n = 25, konfidensgrad 95%, N(2, 1), 100 st konfidensintervall.
## Hur många av dessa kan förväntas inehålla sanna väntevärdet?

intuition: P(väntevärdet inom intervallet) = 1-alpha = 95% => 100 \* 0.95 = 95

Varians vanligt fall: ~4.8
antal värden utanför intervall: vanligt fall ~4.986

Om endast väntevärdet höjs (till 2000) minskar variansen till ~4.6 och antal värden utanför intervall blir 4.999 (högre) och närmare det förväntade antalet
Om endast väntevärdet sänks (till 1/3000) är variansen något lägre än vanligt fall, samma med antal värden utanför intervall (lägre)
Om standardavvikelsen höjs (till 10000) sjunker variansen till ~4.7 och antal värden utanför intervall är högre (5.0115)
Om standardavvikelsen sänks (till 1/10000) sjunker variansen ännu mer till under ~4.7 men antal värden utanför intervall är högre (4.67)
Om konfidensgraden ändras ändras antal värden utanför intervallet och variansen proportionerligt (pga högre/lägre värden). 
om antalet värden som mäts (n) höjs/sänks minskar/höjs variansen något, men antalet värden utanför intervallet är ungefär samma.

# Problem 2

## Skatta Rayleighfördelning mha ML och MK

Ser bra ut, ML och MK skattningarna ger ~0.02 i fel

# Problem 3

## Skatta Konfidensintervall för Rayleighfördelning

Skattning på samma sätt som för problem 2 ger intervall på I = (1.0088405986551325, 1.0194429071193787)

Skattningen verkar korrekt från visuell inspektion

# Problem 4

## Jämförelse av fördelningar hos olika populationer

Från box-plot:en och fördelningarna kan det tydligt ses att fördelningen av födelsevikt för rökande mödrar är förskuten åt vänster (De föder lättare bäbisar).
Från detta kan det ses att rökning hos modern har ett negativt samband med fostrets födelsevikt.

Jag valde att undersöka födelsevikt för foster med tränande mödrar jämfört med de med icke-tränande och kom fram till att mödrar som tränar (mot förväntan) generellt sett föder tynger bebisar.

# Problem 5

## Test av normalitet

Enligt graferna verkar variablarna i stort vara normalfördelade, förutom att moderns vikt verkar vika av lite från linjen.

Enligt jarque bera är endast moderns längd normalfördelad, vilket strider mot min hypotes.

Detta beror troligen på att n är litet, och att vissa extremvärden ökar skevheten


# Problem 6

## Konfidensintervall för skillnad mellan väntevärden för födelsevikter

Konfidensintervallet för skillnaden i vikt mellan icke-rökare(Y) och rökare(X) Y-X blir \[52.72339852669616, 236.625401140022\] med 95% konfidensgrad. Alltså är snittskillnaden mellan vikten av barn från icke-rökare med ~95% sannolikhet inom intervallet \[53, 237\] gram

# Problem 7

## Enkel linjär regression

Residualerna bör rimligtvis vara distribuerade i en normalfördelning kring 0, då felet(residualen) är slumpmässigt och bör vara så jämt fördelat som möjligt => N(0, sqrt(Q0/(n-2))), Vilket i detta fall blir N(0, s) där s är ungefär 0.96. Detta betyder att felet rimligtvis ligger inom \[-1.88, 1.88\] (95% konfidensgrad) => att man i stort kan anta att modellen kommer vara fel med en faktor e^+-1.88 => 1/6.55, 6.55, vilket är stort. Detta beror troligtvis på att antalet mätpunkter är lågt och ganska spridda.

Prediktionen för 2025 ger ~135 986 734 alltså ungefär 136 miljoner