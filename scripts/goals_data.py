"""The raw list of savings goals behind Next Dollar.

Each area of life has default labels, and any goal can override them with
::key=value after its name. build_goals.py turns this file into data/goals.csv
and puts the list into index.html.

Labels:
  s = how the cost behaves:  o = one-time,  m = changes monthly money,  j = just in case
  h = when, for one-time costs:  s = within about 5 years,  l = 5+ years or someday
  n = the old need/want label, kept only to show why it was dropped:
      n = need,  w = want,  d = depends on the person
  a = another bucket the goal could fit (C, L, M, J), or blank

MESSY holds goals typed the way people actually type them, each pointing at the
goal they meant ("typed=>meant"). eval_search.py uses it to score the search.
"""

CATS = [
("Travel", dict(s="o", h="s", n="w", a=""), """
Disney trip with the kids; Hawaii vacation; Europe trip; Japan trip; spring break trip; family beach week;
road trip to national parks; cruise; anniversary getaway; honeymoon::n=d; girls' trip to Vegas; guys' golf trip;
ski trip; camping trip; Mexico all-inclusive; visit family in Nigeria::n=d; trip home for Christmas::n=d;
flight to see grandma::n=d; study abroad for my kid::n=d; Paris for my 40th birthday; Caribbean vacation; Alaska cruise;
bachelorette trip::n=d; bachelor party trip::n=d; summer vacation; weekend getaway; trip to Italy; London trip;
cross-country road trip; Yellowstone trip; Grand Canyon trip; visit college friends in Chicago; Mexico City trip;
Costa Rica; Thailand backpacking; Bali; Iceland northern lights; safari in Kenya; trip to Ghana;
trip to Jamaica to see family::n=d; Philippines trip to see relatives::n=d; Puerto Rico trip; New York City trip;
Las Vegas weekend; New Orleans for Jazz Fest; Coachella; theme park passes; Universal Studios; spring training baseball trip;
Super Bowl trip; World Cup tickets and travel; Olympics trip; eclipse trip; family trip to India::n=d; trip to Korea;
Australia trip; New Zealand trip; Greece; Spain; Portugal; Dubai; Egypt pyramids; Machu Picchu; RV road trip;
backpacking Europe after graduation; retirement celebration trip; babymoon; solo trip; mom's birthday trip;
taking my parents on vacation; kids' first plane trip; visiting family for Thanksgiving::n=d; holiday travel::n=d;
summer trip to grandparents::n=d; trip to see my best friend's new baby::n=d
"""),
("Family & friend gatherings", dict(s="o", h="s", n="d", a=""), """
family reunion; hosting the family reunion; family reunion in Atlanta; class reunion; 20 year high school reunion;
college homecoming; family reunion t-shirts; cousins weekend; hosting Thanksgiving; hosting Christmas dinner; Friendsgiving;
Lunar New Year gathering; Eid celebration; Diwali celebration; Juneteenth cookout; 4th of July BBQ; family cookout;
Easter gathering; Passover seder; hosting my in-laws; parents visiting from abroad; vacation rental for the reunion;
church homecoming; sorority reunion; fraternity reunion; military unit reunion; alumni weekend; friend group trip;
annual girls weekend; book club retreat; family camp; grandparents' 50th anniversary party; Super Bowl party; block party;
neighborhood potluck; Kwanzaa celebration; Dia de los Muertos; family reunion cruise; reunion in the Philippines;
reunion flights for the kids; family photos at the reunion; renting a hall for the reunion; catering for the family reunion;
annual family camping trip; hosting a college friend reunion
"""),
("Weddings & celebrations", dict(s="o", h="s", n="d", a=""), """
my wedding; wedding rings; engagement ring; wedding dress; wedding venue deposit; being a bridesmaid; being in a wedding party;
best man costs; friend's destination wedding; sister's wedding; brother's wedding gift; cousin's wedding travel; bridal shower;
hosting a baby shower; gender reveal party::n=w; quinceañera; sweet 16; bar mitzvah; bat mitzvah; first communion; confirmation;
baptism; christening party; kid's birthday party; my 30th birthday; 40th birthday party; 50th birthday; mom's 60th; dad's 70th birthday;
retirement party; graduation party; high school graduation costs; college graduation trip; prom; senior year expenses::n=n;
anniversary dinner; vow renewal; engagement party; rehearsal dinner; wedding photographer; wedding DJ; wedding catering; elopement;
courthouse wedding; honeymoon fund; housewarming party; debut 18th birthday; traditional wedding in Nigeria; mehndi and sangeet;
tea ceremony; naming ceremony; bris; kids' party rentals; surprise party for my spouse; my kid's wedding someday::h=l
"""),
("Baby & family planning", dict(s="o", h="s", n="n", a=""), """
hospital bill for the birth; birth deductible; crib and nursery; car seat; stroller; baby clothes; diaper stockpile; breast pump;
maternity clothes; prenatal care; doula; midwife; birth center; IVF::n=d; egg freezing::n=d,h=l; fertility treatments::n=d;
adoption fees::n=d; surrogacy::n=d; getting ready to foster; unpaid maternity leave::s=m; paternity leave::s=m; daycare::s=m;
nanny::s=m; nanny share::s=m; second baby::s=m; newborn costs; baby formula::s=m; bigger car for the baby::n=d,a=C;
baby proofing the house; postpartum support; lactation consultant; pediatrician copays::s=j; baby's first year::s=m,a=C;
twins on the way::s=m; night nurse::n=d; newborn photoshoot::n=w; push present::n=w; going down to one income after the baby::s=m;
baby gear; breastfeeding supplies; baby registry extras::n=d
"""),
("Kids", dict(s="o", h="s", n="d", a=""), """
summer camp; sleepaway camp; back to school shopping::n=n; school supplies::n=n; school uniforms::n=n; kids' braces;
kids' glasses::n=n; after school care::s=m,n=n; preschool tuition::s=m; private school tuition::s=m; tutoring::s=m; SAT prep;
college application fees::n=n; college visits; kids' sports fees; travel soccer::s=m; club volleyball::s=m; dance lessons::s=m;
piano lessons::s=m; kid's first phone; laptop for my kid's school::n=n; field trip; 8th grade DC trip; band trip; marching band fees;
school play costs; cheer competition; teen driving insurance::s=m; driver's ed; homecoming dress; prom for my daughter;
senior pictures; cap and gown::n=n; kids' college fund::h=l; 529 for my son::h=l; kids' savings account::h=l; allowance::s=m;
kid's first bike; trampoline::n=w; backyard playset::n=w; kids' Christmas gifts; child support::s=m,n=n; custody lawyer::n=n;
summer childcare::n=n; spring break childcare::n=n; kids' therapy::s=m,n=n; special needs therapy::s=m,n=n; ADHD evaluation::n=n;
speech therapy::s=m,n=n; youth sports tournaments; robotics club; scouts; scout camp; kids' passports::n=n; kid's first car;
study abroad semester; gap year; college move-in; college dorm stuff; my kid's college tuition next year::n=n
"""),
("Education for me", dict(s="o", h="s", n="d", a=""), """
going back to school; finishing my degree; master's degree; MBA; nursing school; PMP certification; coding bootcamp; law school;
LSAT prep; GRE; teaching credential; CDL license; real estate license; cosmetology school; trade school; electrician tools;
welding certification; medical assistant program; CNA class; phlebotomy class; community college classes; online course;
language classes; Spanish immersion program; conference tickets; professional development; textbooks::n=n; laptop for school::n=n;
PhD application fees; bar exam fees; board exam fees; nursing license renewal::n=n; CPA exam; certification renewal::n=n;
UX design course; data analytics certificate; AWS certification; continuing education credits::n=n; dissertation year::s=m;
going back to school full time::s=m
"""),
("Buying a home", dict(s="o", h="l", n="d", a="C"), """
down payment; house down payment in 2 years::h=s,a=L; first home; closing costs::h=s,a=; home inspection::h=s,a=;
earnest money::h=s,a=; condo down payment; townhouse; buying land; building a house; manufactured home; buying a duplex;
house in a better school district; house closer to family; vacation home::n=w,a=; cabin in the mountains::n=w,a=;
beach house::n=w,a=; buying my parents' house; mortgage points::h=s,a=; furnishing a new house::h=s,a=;
appliances for the new house::h=s,a=; home warranty::h=s,n=n,a=; realtor fees to sell::h=s,a=; FHA loan costs::h=s,a=;
first-time homebuyer class::h=s,a=
"""),
("Home repair & upgrades", dict(s="o", h="s", n="n", a=""), """
new roof; HVAC replacement; water heater::s=j; AC repair::s=j; furnace replacement::s=j; plumbing emergency::s=j; foundation repair;
termite treatment; new windows; siding; fence; driveway repaving; kitchen remodel::n=w; bathroom remodel::n=d; new flooring::n=d;
paint the house::n=d; landscaping::n=w; backyard patio::n=w; deck::n=w; pool::n=w; hot tub::n=w; solar panels::n=d,h=l,a=C;
new appliances::n=d; washer and dryer::n=d; new fridge::s=j; dishwasher::n=d; garage door; tree removal; gutters;
sewer line::s=j; mold remediation; earthquake retrofit; hurricane shutters; generator::n=d; ADU::n=d,h=l,a=C; finish the basement::n=w;
garage conversion::n=d; home office::n=d; accessibility ramp; grab bars; new mattress::n=d; new couch::n=w; furniture::n=d;
home security system::n=d; smart home upgrades::n=w; EV charger::n=d; home maintenance fund::s=j; HOA special assessment;
homeowners insurance deductible::s=j; pest control; roof leak::s=j; replace the carpet::n=d; nursery remodel::n=d; storage shed::n=w;
closet organization::n=w; curtains and blinds::n=d; outdoor kitchen::n=w; paint the kids' rooms::n=w; water filter system::n=d
"""),
("Moving & renting", dict(s="o", h="s", n="n", a=""), """
security deposit; first and last month's rent; moving truck; movers; moving across the country; moving to a new city for work;
relocating for a job; apartment application fees; moving out of my parents' house::n=d,a=M; getting my own place::n=d,a=M;
higher rent at the new place::s=m; broker fee; storage unit::s=m; moving to a bigger apartment::n=d,a=M; moving abroad::n=d,a=M;
moving back home::n=d,a=M; moving in with my partner::a=M; renters insurance::s=m; utility deposits; furnishing my first apartment;
moving near my parents::n=d; relocating after a divorce; dorm costs; off-campus housing::s=m; rent increase::s=m; lease break fee;
cleaning deposit; shipping my car cross country; shipping things overseas; temporary housing; hotel between leases; downsizing::a=M;
moving somewhere cheaper::n=d,a=M
"""),
("Car & getting around", dict(s="o", h="s", n="d", a=""), """
new car; used car; car down payment; paying cash for a car; replacing my old car; car for work::n=n; second family car; minivan;
work truck::n=n; electric vehicle; hybrid; motorcycle::n=w; commuter bike; e-bike; car repairs::s=j,n=n; new tires::n=n; brakes::n=n;
transmission::s=j,n=n; car registration::n=n; smog check::n=n; car insurance premium::n=n; car insurance deductible::s=j,n=n;
oil changes::s=m,n=n; car maintenance fund::s=j,n=n; new car battery::s=j,n=n; windshield::s=j,n=n; car detailing::n=w; car wrap::n=w;
new rims::n=w; lift kit::n=w; dream car::h=l,n=w; classic car restoration::h=l,n=w; boat::n=w,h=l; jet ski::n=w; RV::n=w,h=l;
utility trailer; teen's first car; transit pass::s=m,n=n; parking permit::n=n; tolls::s=m; driver's license renewal::n=n;
lease buyout; lease-end fees; accident deductible::s=j,n=n; towing::s=j,n=n; roadside assistance::n=n; getting the car ready for a road trip;
new commute costs::s=m,n=n; rideshare budget::s=m
"""),
("Health (planned)", dict(s="o", h="s", n="n", a=""), """
surgery deductible; knee surgery; hip replacement; dental work; root canal; crowns; dental implants; braces for me::n=d; Invisalign::n=d;
wisdom teeth; glasses; contacts::s=m; LASIK::n=d; hearing aids; physical therapy copays::s=m; therapy sessions::s=m,n=d; counseling::s=m,n=d;
health insurance premiums::s=m; COBRA coverage::s=m; out of pocket max; HSA deductible; mammogram; colonoscopy; dermatologist;
allergy testing; sleep study; CPAP machine; fertility testing::n=d; gender-affirming care; cosmetic surgery::n=w; tummy tuck::n=w;
hair transplant::n=w; botox::n=w,s=m; weight loss program::n=d; nutritionist::n=d; rehab program; wellness retreat::n=d;
medical bills::s=j; ER visit fund::s=j; ambulance bill::s=j; prescriptions::s=m; hospital stay::s=j; urgent care visits::s=j;
travel for medical treatment; hearing test
"""),
("Just in case", dict(s="j", h="s", n="n", a=""), """
emergency fund; job loss cushion; layoff fund; rainy day fund; unexpected bills; car breakdown; broken phone::n=d; laptop dies::n=d;
family emergency travel; legal emergency; lawyer fees; helping family in a crisis; lost income if I get sick; disability waiting period;
storm damage; fire damage deductible; flood cleanup; earthquake kit::s=o; evacuation fund; identity theft recovery; stolen car;
stolen bike; tickets and fines; unpaid time off; furlough; strike fund; gap between jobs; last-minute flight home; surprise wedding invite::s=o,n=d,a=J;
funeral travel; surprise tax bill; underpaid taxes; IRS payment plan::s=m; medical emergency abroad; pet emergency; appliance breakdown;
plumbing leak; power outage costs
"""),
("Pets", dict(s="o", h="s", n="d", a="M"), """
adopt a dog; get a puppy; adopt a cat; get a kitten; pet deposit::a=; pet rent::s=m,a=; vet bills::s=j,a=; emergency vet::s=j,a=;
pet surgery::s=j,a=; spay or neuter::a=; dog training::a=; pet insurance::s=m,a=; dog walker::s=m,a=; doggy daycare::s=m,a=;
boarding while we travel::a=; pet food::s=m,a=; aquarium setup::n=w; horse::n=w; horse boarding::s=m,a=,n=w; backyard chickens;
pet bird; reptile setup::n=w; pet dental cleaning::a=; senior dog care::s=m,a=; pet cremation::s=j,a=; fence for the dog::a=;
pet sitter::a=; grooming::s=m,a=; pet vaccines::a=,n=n; microchip::a=,n=n; crate and dog supplies::a=; cat tree::n=w,a=;
dog stroller::n=w,a=; flying with my pet::a=
"""),
("Tech", dict(s="o", h="s", n="d", a=""), """
new phone; iPhone upgrade::n=w; new laptop; work laptop::n=n; gaming PC::n=w; PS5::n=w; Xbox::n=w; Nintendo Switch::n=w; iPad;
smartwatch::n=w; headphones::n=w; new TV::n=w; home theater::n=w; camera::n=w; drone::n=w; VR headset::n=w; printer;
home wifi upgrade; monitor for working from home::n=n; standing desk; office chair; external hard drive; software subscription::s=m;
Adobe subscription::s=m; phone bill::s=m,n=n; replacing a cracked phone::s=j; tablet for the kids; e-reader::n=w; sound system::n=w;
smart speakers::n=w; 3D printer::n=w; sewing machine::n=w; guitar::n=w; keyboard piano::n=w; DJ equipment::n=w; podcast mic;
streaming setup::n=w; photography gear::n=w; computer for my business::n=n; phone for my mom
"""),
("Hobbies & fun", dict(s="o", h="s", n="w", a=""), """
concert tickets; Beyoncé tour; Taylor Swift tickets; Broadway show; season tickets::s=m; Lakers game; Dodgers tickets; comedy show;
festival pass; theme park annual pass; golf clubs; golf membership::s=m; tennis lessons; surfboard; skis; snowboard gear; camping gear;
kayak; fishing gear; hunting gear; road bike; mountain bike; art supplies; pottery class; painting class; cooking class; wine club::s=m;
photography class; dance classes; salsa lessons; music lessons; drum set; knitting supplies; garden supplies; greenhouse;
woodworking tools; quilting; sneaker collection; trading cards; LEGO sets; board games; video games; books; Comic-Con; cosplay;
anime convention; Renaissance faire; spa day; massage::n=d; nice dinner out; tasting menu; bucket list trip::h=l; skydiving;
scuba certification; flying lessons; pilot's license::n=d; marathon registration; triathlon; Hyrox race; Disneyland annual pass
"""),
("Career & business", dict(s="o", h="s", n="d", a=""), """
start a business::h=l,a=C; side hustle startup costs; food truck::h=l,a=C; open a salon::h=l,a=C; bakery::h=l,a=C;
LLC formation::n=n; business license::n=n; website for my business; business equipment; inventory; trademark; business insurance::s=m;
hiring my first employee::s=m; coworking space::s=m; work clothes for a new job::n=n; interview outfit::n=n; career coach;
resume writer; job search fund::s=j; relocating for a job::a=M; networking events; professional headshots; conference travel;
publishing my book; self-publishing; recording an album; film project; Etsy shop; Amazon FBA inventory; franchise fee::h=l;
buying a business::h=l; tools for my trade::n=n; commercial kitchen rental::s=m; quitting to freelance::s=m; pay cut for a career change::s=m;
unpaid internship::s=m; sabbatical::s=m; going part time::s=m; leave from my business::s=m; self-employed taxes::n=n;
quarterly taxes::n=n; accountant fees::n=n; business laptop::n=n; podcast launch; photography business gear
"""),
("Giving & faith", dict(s="o", h="s", n="d", a=""), """
tithing::s=m; church building fund; mission trip; Hajj; Umrah; pilgrimage to Jerusalem; zakat; charity donation; donor advised fund::h=l;
sponsoring a child::s=m; sending money home::s=m; remittances to family::s=m; helping my parents with rent::s=m;
helping my sister through college::s=m; GoFundMe for a friend; disaster relief donation; alumni donation; school fundraiser;
church anniversary; religious retreat; Bible camp for the kids; Catholic school::s=m; temple dues::s=m; synagogue membership::s=m;
hosting iftar during Ramadan; Christmas giving; toy drive; paying for a relative's funeral; scholarship fund::h=l; giving circle::s=m
"""),
("Caring for family & end of life", dict(s="o", h="s", n="n", a=""), """
funeral costs; my own funeral plan::h=l; cremation; burial plot::h=l; headstone; memorial service; celebration of life;
flights for a funeral::s=j; mom's funeral::s=j; dad's medical bills::s=j; caring for an aging parent::s=m; assisted living for mom::s=m;
home health aide::s=m; nursing home::s=m; adult day care for dad::s=m; moving a parent in with us::s=m; accessibility changes for my parents' house;
hospice; long-term care insurance::s=m; life insurance premium::s=m; will and trust; estate planning attorney; power of attorney paperwork;
probate costs; clearing out my parent's house; caring for a sibling::s=m; long-term care for my disabled child::h=l,s=m;
unpaid caregiver leave::s=m; respite care::s=m; grief counseling::n=d,s=m
"""),
("Yearly & seasonal bills", dict(s="o", h="s", n="n", a=""), """
property tax bill; six-month car insurance premium; annual renters insurance; annual life insurance premium; Costco membership;
Amazon Prime; annual subscriptions; HOA dues; tax preparer; April tax bill; estimated taxes; DMV registration; professional dues;
license renewal; passport renewal; school registration fees; annual checkup copays; holiday spending; back to school season;
birthday gifts all year::n=d; wedding season gifts::n=d; Christmas; summer electric bill spike; winter heating bill; water bill;
trash bill; website domain and hosting; union dues; bar dues; medical license renewal; annual gym fee::n=d; AAA membership;
warehouse club membership; software licenses; kids' activity registration::n=d; homeowners insurance premium; umbrella policy;
pet license; fishing license::n=w; hunting license::n=w
"""),
("Big life changes", dict(s="m", h="s", n="d", a=""), """
divorce::n=n,a=C; separation::a=C; moving out after a breakup::n=n,a=C; getting married and combining money; moving in together;
having a baby::n=n; kids leaving for college; empty nest; retirement::h=l; career change; going back to school full time;
job loss::s=j; new job with lower pay; taking a sabbatical; going part time; becoming a stay-at-home parent; spouse going back to school;
spouse losing their job::s=j; caring for a sick partner::n=n; becoming disabled::n=n; chronic illness::n=n; moving to a new country::a=C;
immigration costs::s=o,n=n; becoming a caregiver::n=n; blending families; adopting a teenager; military deployment; leaving the military;
starting residency; losing a roommate; roommate moving out; partner losing income::s=j; going from two incomes to one;
starting a new job with a longer commute; becoming an empty nester
"""),
("Personal care & style", dict(s="o", h="s", n="w", a=""), """
new wardrobe; work clothes::n=d; winter coat::n=d; designer bag; sneakers; braids::s=m; wig; hair salon::s=m; nails::s=m; lashes::s=m;
skincare; microblading; tattoo; tattoo removal; teeth whitening; veneers; jewelry; watch; new glasses frames; perfume;
suit for a wedding::n=d; formal dress; shoes; makeup; barber::s=m; gym clothes; new clothes after the baby::n=d; maternity wardrobe::n=d;
new prescription glasses::n=n; laser hair removal; massage membership::s=m; spa weekend; personal stylist; photoshoot; closet refresh
"""),
("Legal & paperwork", dict(s="o", h="s", n="n", a=""), """
passport; visa fees; green card fees; citizenship application; name change; divorce lawyer; custody case; writing a will; setting up a trust;
immigration lawyer; traffic ticket::s=j; court fees::s=j; bankruptcy attorney; credit repair; tax attorney; small claims court::s=j;
notary fees; birth certificate copy; REAL ID; marriage license; prenup; tenant lawyer::s=j; background check fees; security clearance;
expungement fees
"""),
("Sports & fitness", dict(s="o", h="s", n="w", a=""), """
gym membership::s=m,n=d; home gym; Peloton; squat rack; dumbbells; running shoes::n=d; marathon travel; race entry fees; CrossFit::s=m;
yoga teacher training; pilates classes::s=m; personal training::s=m; boxing classes::s=m; jiu jitsu::s=m; martial arts for the kids::s=m;
swim lessons::n=d; golf lessons; softball league; bowling league::s=m; pickleball paddles; tennis racket; climbing gym::s=m; ski pass;
hiking gear; backpacking trip; fitness retreat; weight loss coaching::s=m; sports physical::n=n; supplements::s=m; bodybuilding show
"""),
("Gifts & holidays", dict(s="o", h="s", n="d", a=""), """
Christmas gifts; holiday gifts; birthday gifts; Mother's Day; Father's Day; Valentine's Day; anniversary gift; graduation gifts;
wedding gifts; baby shower gifts; teacher gifts; Secret Santa; Hanukkah gifts; Eid gifts; Lunar New Year red envelopes; Diwali gifts;
Halloween costumes::n=w; holiday decorations::n=w; Thanksgiving dinner; Christmas tree; holiday cards; gift for my spouse;
retirement gift; farewell gift for my boss; family Christmas trip; New Year's Eve party; Easter baskets; birthday dinner;
kids' birthday presents; stocking stuffers; gas for holiday driving; gift for my parents' anniversary; Black Friday deals::n=w
"""),
("Long-term goals", dict(s="o", h="l", n="d", a=""), """
early retirement; retiring at 55; financial independence; investment property; rental property; paying off my mortgage early;
kids' college; grandkids' college; generational wealth; trust fund for the kids; buying my parents a house; land in my home country;
retiring abroad; retirement home; beach house in retirement::n=w; sabbatical year in five years; world trip in retirement::n=w;
boat in retirement::n=w; vacation home someday::n=w; Coast FI; stock portfolio; brokerage account; Roth IRA; HSA for retirement;
my dream house; building an ADU to rent; buying a farm; moving to Europe someday; helping the kids buy their first home
"""),
]

# Messy, typed-by-a-real-person versions (tests whether a search box can still match them)
MESSY = """
disney w kids=>Disney trip with the kids; hawaii!!=>Hawaii vacation; bday trip for mom=>mom's birthday trip;
vegas bachelorette=>bachelorette trip; family reunion $$=>family reunion; reunion tshirts=>family reunion t-shirts;
xmas gifts=>Christmas gifts; xmas travel=>holiday travel; new roof asap=>new roof; ac broke=>AC repair; car stuff=>car maintenance fund;
new(er) car=>used car; tires + brakes=>new tires; the wedding=>my wedding; our wedding next june=>my wedding;
my sisters wedding=>sister's wedding; baby #2=>second baby; daycare $=>daycare; ivf round 2=>IVF; house fund=>down payment;
downpayment=>down payment; move out=>moving out of my parents' house; new apt=>security deposit; grad school=>master's degree;
pmp exam=>PMP certification; puppy!!=>get a puppy; vet=>vet bills; laptop=>new laptop; phone=>new phone; ps5=>PS5;
concert=>concert tickets; beyonce tix=>Beyoncé tour; biz startup=>start a business; side hustle=>side hustle startup costs;
tithe=>tithing; send $ home=>sending money home; moms care=>caring for an aging parent; funeral=>funeral costs;
taxes=>April tax bill; car reg=>car registration; divorce=>divorce; quit my job=>quitting to freelance; braids=>braids;
passport=>passport; gym=>gym membership; retire early=>early retirement; rental prop=>rental property;
emergency $$=>emergency fund; just in case money=>rainy day fund; cushion=>emergency fund; school stuff for kids=>school supplies
"""
