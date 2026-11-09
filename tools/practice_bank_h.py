from practice_lib import *
import math

topic("catalysis", "Catalysis &amp; ammonia production", "unit15", "Quiz 8",
      "Quiz 8 (Fall 2024) mixes catalyst reasoning (Sabatier volcano, CO vs O<sub>2</sub> binding) with equilibrium. Recipe: a catalyst gives a path with a <b>lower E<sub>a</sub></b> and leaves "
      "<b>&Delta;H, &Delta;G and K unchanged</b>; <b>homogeneous</b> = same phase as the reactants, <b>heterogeneous</b> = a different phase (a solid surface), <b>enzymes</b> = protein catalysts; "
      "Haber&ndash;Bosch = Fe, 400&ndash;500 &deg;C, high P, liquefy NH<sub>3</sub>, recycle N<sub>2</sub> + H<sub>2</sub>.")

mc("catalysis-1", "catalysis", 1, "L25 &middot; Unit 12",
   "What does adding a catalyst to the reaction N<sub>2</sub> + 3H<sub>2</sub> &rlarr; 2NH<sub>3</sub> change?",
   ["It lowers the activation energy, so equilibrium is reached faster; K and &Delta;H are unchanged", "It raises K, so more NH<sub>3</sub> is present at equilibrium", "It makes &Delta;H more negative", "It is consumed and must be replaced each pass"],
   "<p>A catalyst provides another path with a lower E<sub>a</sub> for the forward <em>and</em> reverse reactions. &Delta;H, &Delta;G and K (set by the start and end states) do not change, and the catalyst is regenerated.</p>")

mc("catalysis-2", "catalysis", 1, "L25 slide 5",
   "Ertl&rsquo;s mechanism for ammonia synthesis on iron: what happens first?",
   ["N<sub>2</sub> and H<sub>2</sub> adsorb on the surface and the N&equiv;N and H&ndash;H bonds split into surface atoms", "NH<sub>3</sub> forms in the gas phase and then lands on the iron", "Three H atoms bond to one N<sub>2</sub> molecule without splitting it", "The iron dissolves into the gas"],
   "<p>On the surface N<sub>2</sub> and H<sub>2</sub> dissociate into adsorbed atoms; N&ndash;H bonds then form stepwise (N &rarr; NH &rarr; NH<sub>2</sub> &rarr; NH<sub>3</sub>) and NH<sub>3</sub> desorbs.</p>")

mc("catalysis-3", "catalysis", 2, "L25 slide 5",
   "In the order on the slide, how does NH<sub>3</sub> form on the iron surface?",
   ["N(ad) &rarr; NH(ad) &rarr; NH<sub>2</sub>(ad) &rarr; NH<sub>3</sub>(ad) &rarr; NH<sub>3</sub>(g)", "NH<sub>3</sub>(ad) &rarr; NH<sub>2</sub>(ad) &rarr; NH(ad) &rarr; N(ad)", "N(ad) &rarr; NH<sub>3</sub>(ad) directly, in one step", "N<sub>2</sub>(g) &rarr; NH<sub>3</sub>(g) directly"],
   "<p>Hydrogen atoms are added to the nitrogen atom one at a time: N, NH, NH<sub>2</sub>, NH<sub>3</sub>. Then the finished molecule leaves the surface.</p>")

dE = 1129 - 1400
num("catalysis-4", "catalysis", 2, "L25 slide 5",
    "On the slide, taking &frac12;N<sub>2</sub> + 3/2H<sub>2</sub> to free atoms N + 3H costs 1129 kJ/mol, but the adsorbed atoms N(ad) + 3H(ad) lie 1400 kJ/mol below free atoms. What is the net energy change (kJ/mol) for gas &rarr; adsorbed atoms?",
    dE, "kJ/mol",
    "<p>Net = +1129 (break bonds) &minus; 1400 (form bonds to the iron) = <b>%d kJ/mol</b>. The surface pays back the cost of breaking N&equiv;N, so the splitting step becomes nearly free: that is what the catalyst does.</p>" % dE,
    text="%d kJ/mol" % dE)

num("catalysis-5", "catalysis", 1, "L25 slide 5",
    "The slide marks &Delta;H = 46 kJ/mol (released) for forming one mole of NH<sub>3</sub>. What is &Delta;H, in kJ, for N<sub>2</sub> + 3H<sub>2</sub> &rarr; 2NH<sub>3</sub>?",
    -92.0, "kJ",
    "<p>The equation makes 2 mol NH<sub>3</sub>: 2 &times; (&minus;46) = <b>&minus;92 kJ</b> (exothermic; the same &minus;92 kJ used in Unit 13).</p>",
    text="-92 kJ")

mc("catalysis-6", "catalysis", 1, "L25 slide 6",
   "In the Haber&ndash;Bosch plant, how is NH<sub>3</sub> separated from the unreacted N<sub>2</sub> and H<sub>2</sub>?",
   ["It is cooled until the polar NH<sub>3</sub> condenses to a liquid; the N<sub>2</sub> and H<sub>2</sub> stay gaseous and are recycled", "It is filtered out as a solid", "It dissolves in the iron catalyst", "It is burnt"],
   "<p>Ammonia is polar and hydrogen-bonds, so its boiling point is much higher than that of N<sub>2</sub> or H<sub>2</sub>; cooling condenses it. The remaining gases are circled back to the reactor.</p>")

mc("catalysis-7", "catalysis", 2, "L25 slide 6 &middot; Unit 14",
   "Removing liquid NH<sub>3</sub> from the loop, so the reaction can continue, works because&hellip;",
   ["it keeps Q below K, so the net reaction keeps running to the right", "it raises K", "it lowers the activation energy", "it makes the reaction endothermic"],
   "<p>Q = [NH<sub>3</sub>]&sup2;/([N<sub>2</sub>][H<sub>2</sub>]&sup3;). Taking NH<sub>3</sub> away makes Q small again; Q &lt; K means the reaction proceeds right. K itself depends only on temperature.</p>")

mc("catalysis-8", "catalysis", 3, "L25 slide 6 &middot; Units 12, 14",
   "The reactor is run at 400&ndash;500 &deg;C even though the reaction is exothermic. Why not much lower?",
   ["High T gives a usable rate, but also lowers K; the temperature is a compromise between rate and yield", "High T raises K for an exothermic reaction", "The catalyst only works below 100 &deg;C", "NH<sub>3</sub> is solid above 100 &deg;C"],
   "<p>Exothermic &rarr; K falls as T rises (less NH<sub>3</sub> at equilibrium). But at low T the rate is far too slow even with a catalyst. So a moderate T, high pressure and recycling together give a workable process.</p>")

mc("catalysis-9", "catalysis", 2, "L25 slide 6",
   "Which temperature range does the Haber&ndash;Bosch catalyst chamber on the slide operate at?",
   ["400 to 500 &deg;C", "25 to 50 &deg;C", "1000 to 1200 &deg;C", "&minus;100 to 0 &deg;C"],
   "<p>The slide labels the catalyst chamber 400 to 500 &deg;C.</p>")

glob = 500 / 0.018
num("catalysis-10", "catalysis", 2, "L25 slide 7",
    "Ammonia production emits about 500 million tons of CO<sub>2</sub> a year, which the slide says is about 1.8% of global CO<sub>2</sub> emissions. What total global emission (in million tons) does that imply?",
    glob, "Mt",
    "<p>If 1.8%% = 500 Mt, total = 500 / 0.018 = <b>%s Mt</b> (about 28 billion tons).</p>" % fmt(glob, 4),
    tol=0.02, text="%s Mt" % fmt(glob, 4))

mc("catalysis-11", "catalysis", 1, "L25 slide 7",
   "Where does the hydrogen for ammonia mostly come from, and by which reaction?",
   ["Steam methane reforming: CH<sub>4</sub> + H<sub>2</sub>O &rarr; CO + 3H<sub>2</sub>", "Burning ammonia", "Electrolysis of seawater", "Heating nitrogen"],
   "<p>Steam methane reforming (Ni catalyst) makes H<sub>2</sub> and CO; it accounts for over 80% of the energy needed and is the main source of the CO<sub>2</sub>.</p>")

mc("catalysis-12", "catalysis", 2, "L25 slide 8",
   "Which list gives the three jobs of a catalytic converter?",
   ["Oxidize CO to CO<sub>2</sub>; oxidize unburnt fuel to CO<sub>2</sub>; reduce NO<sub>x</sub> to N<sub>2</sub>", "Reduce CO to carbon; oxidize NO<sub>x</sub>; burn N<sub>2</sub>", "Convert CO<sub>2</sub> to CO; make NO<sub>x</sub>; filter soot", "Oxidize N<sub>2</sub>; reduce CO<sub>2</sub>; cool the exhaust"],
   "<p>CO and unburnt fuel are oxidized; nitrogen oxides (brown smog) are reduced to N<sub>2</sub> using some of the fuel or CO. Catalysts: Rh, Pt, a little Pd, plus CeO<sub>2</sub> and &gamma;-alumina.</p>")

mc("catalysis-13", "catalysis", 2, "L25 slide 8 &middot; Quiz 7",
   "Why does a car emit more pollutants in the first minute after a cold start?",
   ["The converter is too cold for the reactions to run quickly: the rate constant is small at low T (Arrhenius)", "The catalyst has been used up", "&Delta;G of the reactions is positive when cold", "Cold fuel contains more nitrogen"],
   "<p>The converter reactions still need to clear E<sub>a</sub>; at low temperature k = Ae<sup>&minus;E<sub>a</sub>/RT</sup> is tiny until the exhaust has heated the catalyst.</p>")

mc("catalysis-14", "catalysis", 1, "L25 slides 9, 14",
   "A solid iron catalyst is used with N<sub>2</sub> and H<sub>2</sub> gases. A dissolved rhodium complex is used with liquid reactants. Which is which?",
   ["Iron: heterogeneous; rhodium complex: homogeneous", "Iron: homogeneous; rhodium complex: heterogeneous", "Both are homogeneous", "Both are heterogeneous"],
   "<p>Homogeneous = catalyst in the same phase as the reactants (typically in solution). Heterogeneous = different phase (solid surface with gases).</p>")

mc("catalysis-15", "catalysis", 2, "L25 slide 14",
   "Which statement about homogeneous catalysts is true?",
   ["They collide with reactants more often, but are hard to recover and less stable, so they suit lower-temperature processes", "They are easy to filter out of the product", "They work only at very high temperature", "They are always solids"],
   "<p>Dissolved organo-metallic catalysts are well mixed with the reactants (frequent collisions, activated complexes of lower energy), but separating them afterwards is very hard and they are less stable.</p>")

mc("catalysis-16", "catalysis", 1, "L25 slide 9",
   "Match the process to its catalyst: Haber process, contact process, Ostwald process.",
   ["Fe (with K<sub>2</sub>O, Al<sub>2</sub>O<sub>3</sub>); V<sub>2</sub>O<sub>5</sub> or Pt; Pt and Rh", "V<sub>2</sub>O<sub>5</sub>; Pt and Rh; Fe", "Ni; Fe; Pt", "Pt; Fe; Ni"],
   "<p>Haber: Fe. Contact (SO<sub>2</sub> &rarr; SO<sub>3</sub> for H<sub>2</sub>SO<sub>4</sub>): V<sub>2</sub>O<sub>5</sub> or Pt. Ostwald (NH<sub>3</sub> &rarr; NO &rarr; HNO<sub>3</sub>): Pt and Rh. (Steam reforming uses Ni.)</p>")

mc("catalysis-17", "catalysis", 1, "L25 slide 10",
   "How do enzymes compare with industrial catalysts?",
   ["Extremely specific and fast (up to 10<sup>17</sup>&times;), but expensive, hard to adapt and unstable, so limited industrial use", "Cheap and stable at 500 &deg;C", "Slower but more general", "They lower K"],
   "<p>Most enzymes are proteins, often metallo-proteins. They can make a reaction run as fast as diffusion, but they are fragile and costly to use at scale.</p>")

t0 = 3.15e7 / 1e17
num("catalysis-18", "catalysis", 2, "L25 slide 10",
    "A reaction would take one year (3.15&times;10<sup>7</sup> s) without a catalyst. An enzyme speeds it up by 10<sup>17</sup>. How long does it take with the enzyme, in seconds?",
    t0, "s",
    "<p>Time = 3.15&times;10<sup>7</sup> s / 10<sup>17</sup> = <b>%s s</b>, about a third of a nanosecond. At that speed the reaction is limited by how fast molecules diffuse into the active site, not by the chemistry.</p>" % fmt(t0, 3),
    text="%s s" % fmt(t0, 3))

mc("catalysis-19", "catalysis", 2, "L25 slide 10",
   "How can an enzyme make an uphill (&Delta;G &gt; 0) reaction go?",
   ["By coupling it to a highly spontaneous reaction of a co-factor such as ATP, so the combined &Delta;G is negative", "By raising K of the uphill reaction", "By removing the activation energy completely", "By changing &Delta;H of the reactants"],
   "<p>Coupling: an uphill step runs by &ldquo;sacrificing&rdquo; a very reactive co-factor (ATP, NADPH). The total &Delta;G = &Delta;G<sub>uphill</sub> + &Delta;G<sub>ATP</sub> is negative.</p>")

mc("catalysis-20", "catalysis", 1, "L25 slide 11",
   "What is nitrogen fixation?",
   ["Moving N<sub>2</sub> from the atmosphere into molecular compounds (such as NH<sub>3</sub>/NH<sub>4</sub><sup>+</sup>) in soil", "Removing nitrogen from fertilizer", "Burning nitrogen in air", "Freezing N<sub>2</sub>"],
   "<p>Natural nitrogen-fixing bacteria in legume root nodules and in soil do this; industrially, the Haber&ndash;Bosch process does it.</p>")

mc("catalysis-21", "catalysis", 2, "L25 slide 11",
   "In the soil nitrogen cycle, which pathway is right?",
   ["N<sub>2</sub> &rarr; NH<sub>4</sub><sup>+</sup> (fixing bacteria) &rarr; NO<sub>2</sub><sup>&minus;</sup> &rarr; NO<sub>3</sub><sup>&minus;</sup> (nitrifying bacteria); plants assimilate; denitrifying bacteria return N<sub>2</sub>", "N<sub>2</sub> &rarr; NO<sub>3</sub><sup>&minus;</sup> &rarr; NH<sub>4</sub><sup>+</sup> by plants", "NH<sub>4</sub><sup>+</sup> &rarr; N<sub>2</sub> by fixing bacteria", "N<sub>2</sub> is made only by lightning"],
   "<p>Fixation makes ammonium; nitrifying bacteria oxidise it to nitrite then nitrate; plants take up nitrogen (assimilation); decomposers give back ammonium; denitrifiers turn nitrate into N<sub>2</sub> again.</p>")

mc("catalysis-22", "catalysis", 2, "L25 slide 12",
   "The active site of nitrogenase contains which metals?",
   ["Iron and molybdenum (Fe<sub>7</sub>MoS<sub>9</sub>C cluster)", "Platinum and rhodium", "Nickel and palladium", "Copper and zinc only"],
   "<p>The FeMo cofactor is an iron&ndash;sulfur&ndash;molybdenum cluster, Fe<sub>7</sub>MoS<sub>9</sub>C, inside a large protein dimer.</p>")

num("catalysis-23", "catalysis", 2, "L25 slide 13",
    "N<sub>2</sub> + 8H<sup>+</sup> + 8e<sup>&minus;</sup> + 16 MgATP &rarr; 2NH<sub>3</sub> + H<sub>2</sub> + 16 MgADP + 16 P<sub>i</sub>. How many ATP are used per NH<sub>3</sub> formed?",
    8.0, "ATP",
    "<p>16 ATP make 2 NH<sub>3</sub> (plus one H<sub>2</sub>), so 16/2 = <b>8 ATP per NH<sub>3</sub></b>.</p>",
    text="8")

mc("catalysis-24", "catalysis", 2, "L25 slide 18",
   "Compare N<sub>2</sub> + 3H<sub>2</sub> &rlarr; 2NH<sub>3</sub> with NH<sub>4</sub><sup>+</sup> &rlarr; NH<sub>3</sub> + H<sup>+</sup>. What happens to the oxidation state of nitrogen?",
   ["Synthesis: 0 to &minus;3; recovery: stays at &minus;3", "Synthesis: stays at 0; recovery: 0 to &minus;3", "Both: +3 to &minus;3", "Both stay at &minus;3"],
   "<p>In N<sub>2</sub> nitrogen is 0; in NH<sub>3</sub> and NH<sub>4</sub><sup>+</sup> it is &minus;3. Making ammonia reduces N (energy and catalyst needed). Recovery only moves a proton, so N stays at &minus;3.</p>")

mc("catalysis-25", "catalysis", 3, "L25 slides 18&ndash;19 &middot; extra",
   "In NH<sub>4</sub><sup>+</sup> &rlarr; NH<sub>3</sub> + H<sup>+</sup>, what happens if H<sup>+</sup> is removed (higher pH)?",
   ["The equilibrium shifts right and NH<sub>3</sub> is released", "The equilibrium shifts left", "K increases", "Nothing, because H<sup>+</sup> is not in K"],
   "<p>Removing a product makes Q &lt; K, so the reaction proceeds right and releases NH<sub>3</sub> (Le Ch&acirc;telier). K itself is unchanged.</p>")

mc("catalysis-26", "catalysis", 3, "L25 slide 5 &middot; extra",
   "A good catalyst surface binds N atoms strongly enough to break N&equiv;N but not so strongly that NH<sub>3</sub> cannot leave. What is this idea called?",
   ["The Sabatier principle (a volcano plot of activity against binding strength)", "Le Ch&acirc;telier&rsquo;s principle", "Hund&rsquo;s rule", "The Born&ndash;Haber cycle"],
   "<p>Too weak a grip: reactants never split. Too strong: products stay stuck. Activity peaks at intermediate binding, a volcano shape.</p>")

selfq("catalysis-27", "catalysis", 2, "L25 slides 9, 10, 14",
      "In a few lines compare heterogeneous, homogeneous and enzymatic catalysis: where is the catalyst, one strength, one weakness of each.",
      "<p><b>Model answer.</b> <b>Heterogeneous:</b> a solid (Fe, Pt/Rh, V<sub>2</sub>O<sub>5</sub>) with gas reactants; stable at high T and easy to separate; only the surface works. <b>Homogeneous:</b> an organo-metallic complex dissolved with the reactants; frequent collisions and tunable electronic properties; very hard to recover and less stable (low-T processes). <b>Enzymatic:</b> a protein with an active site; extremely specific and up to 10<sup>17</sup> times faster, can couple uphill reactions with ATP; expensive, unstable and hard to adapt, so limited industrial use.</p>")

selfq("catalysis-28", "catalysis", 3, "L25 slides 5&ndash;7",
      "Explain why the Haber&ndash;Bosch process uses an iron catalyst, 400&ndash;500 &deg;C, high pressure, condensation of NH<sub>3</sub> and a recycle loop. What does the catalyst <em>not</em> do?",
      "<p><b>Model answer.</b> Fe adsorbs N<sub>2</sub> and H<sub>2</sub> and splits them into surface atoms, lowering E<sub>a</sub> so the reaction is fast enough. The reaction is exothermic, so higher T lowers K, but low T is too slow: 400&ndash;500 &deg;C is the compromise. High pressure favours the side with fewer gas moles (4 &rarr; 2). Condensing the polar NH<sub>3</sub> removes product (Q &lt; K) and recycling the unreacted N<sub>2</sub> and H<sub>2</sub> raises the overall yield. The catalyst does <b>not</b> change K, &Delta;H, &Delta;G or the equilibrium yield; it only speeds up approach to equilibrium.</p>")
