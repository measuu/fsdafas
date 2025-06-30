from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import DateTime, ForeignKey, String, Text, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash

from settings import Base, Session


class User(UserMixin, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    is_admin: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"User: {self.username}"

    @staticmethod
    def get(user_id: int):
        with Session() as conn:
            stmt = select(User).where(User.id == user_id)
            user = conn.scalar(stmt)
            if user:
                return user

    @staticmethod
    def get_by_username(username):

        with Session() as conn:
            stmt = select(User).where(User.username == username)
            user = conn.scalar(stmt)
            return user if user else None


class Team(Base):
    __tablename__ = "teams"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    logo_url: Mapped[str] = mapped_column(String(250))
    trophies: Mapped[int] = mapped_column(nullable=True)
    descr: Mapped[str] = mapped_column(Text)
    players: Mapped[str] = mapped_column(nullable=True)


class Player(Base):
    __tablename__ = "players"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    nickname: Mapped[str] = mapped_column(String(150))
    age: Mapped[int] = mapped_column(nullable=False)
    years: Mapped[str] = mapped_column(String(150))
    photo_url: Mapped[str] = mapped_column(String(250))
    trophies: Mapped[int] = mapped_column(nullable=True)
    mvp: Mapped[int] = mapped_column(nullable=True)
    descr: Mapped[str] = mapped_column(Text)


def init_db():
    base = Base()
    base.drop_db()
    base.create_db()

    user_admin = User(
        username="admin",
        email="ax@gmail.com",
        password=generate_password_hash("admin"),
        is_admin=True,
    )

    navi = Team(
        name="Natus Vincere(NAVI)",
        logo_url="https://photobooth.cdn.sports.ru/preset/news/0/6c/e1d4129b64425a71553a13791652f.png",
        trophies=37,
        descr="Natus Vincere— підрозділ української кіберспортивної команди Natus Vincere з гри Counter-Strike, створений 2009 року. У 2010 році команда вперше в історії кіберспорту виграла три головні турніри протягом одного року — Intel Extreme Masters, Electronic Sports World Cup і World Cyber Games 2010. На мейджор-турнірах із CS:GO NAVI тричі доходида до фіналу (Cluj-Napoca 2015, MLG Columbus 2016 та Major 2018), допоки 2021 року команда не стала чемпіоном на PGL Major Scoterholm 2021. 2024 року команда виграла другий мейджор-турнір (і перший в історії Counter-Strike 2) — PGL CS2 Major Copenhagen 2024. Команду створили в грудні 2009 року. Після розпаду українського проєкту KerchNET (2013), колишніх гравців команди підтримав відомий казахстанський бізнесмен та організатор кібертурнірів Мурат «Арбалет» Жумашевич Тулемаганбетов. Зібрану ним команду було названо «Arbalet.UA». До її складу увійшли Данило «Zeus» Тесленко та Іван «Edward» Сухар'єв, Сергій «starix» Іщук, Арсеній «Ceh9» Триноженко та Єгор «markeloff» Маркелов. Менеджером команди став Олександр «ZeroGravity» Кохановський. У лютому був оголошений конкурс на назву команди, що тоді виступала як «Arbalet.UA» або «Na'Vi». За підсумками голосування на сайті hltv.org, переможцем став португалець Bruno «hArt1k» Estevens, який запропонував назву «Team Vincit», похідним від якого стала фінальна назва «Natus Vincere» (з лат. — «народжені перемагати»), що дозволило залишити тег без змін — «Na'Vi». Найкращим роком в історії NAVI по CS беззаперечно є 2021. У 2021 році команда вперше перемогла на мейджор-турнірі PGL Major Stockholm 2021, ставши єдиною командою, що виграла турнір без жодної втраченої карти. Склад гравців у 2021: s1mple(снайпер/AWPer), electronic(Entry Fragger), Boombl4(капітан/In-Game Leader (IGL)), Perfecto(Support), b1t(Ріфлер/Rifler). s1mple став найкращим гравцем світу за версією HLTV – І показав, можливо, найкращу індивідуальну форму в історії гри.",
        players="b1t - Rifler, Aleksib - In-game Leader (IGL), iM - Rifler, jL - Entry Fragger / Rifler, w0nderful - AWP-cнайпер (AWPer) B1ad3 - Головний тренер",
    )

    fnatic = Team(
        name="Fnatic",
        logo_url="https://images.cybersport.ru/images/details-logo/plain/4d/4db63d7a117658ce883867d9266d8786.png",
        trophies=23,
        descr="Fnatic — професійна кіберспортивна організація зі штаб-квартирою в Лондоні, Велика Британія. Заснована 23 липня 2004 року. Коли Fnatic перейшли на Counter-Strike: Global Offensive, вони стали однією з найкращих команд у світі. Одразу ж після цього Fnatic оголосили про підписання Xyp9x & JOKERN. З новим ростером команда здобула 3/4 місце на EMS Season 1 Finals. Наприкінці 2013 року, Fnatic виграли свій перший великий турнір в Counter-Strike: Global Offensive під керівництвом свого нового лідера, Маркуса «pronax» Воллстена. У 2014 році Fnatic взяли 2 гравців екс-LGB — Олофа «olofmeister» Кайбьєраі Фредді «KRiMZ» Йоханссона. На цьому перемоги команди не скінчилися, вони здобули чемпіонство на ESL One Катовіце 2015, а 24 серпня 2015 року Fnatic перемогли на ESL One Cologne. Через ці великі перемоги та ще 11 інших міжнародних титулів, деякі вважають Fnatic найсильнішою командою, з коли-небудь зібраних в історії CS:GO. У листопаді 2015 року, після декількох провальних виступів, pronax вирішив взяти паузу від професійного CS: GO. Він був замінений Деннісом «Dennis» Едманом, який перейшов до Fnatic з G2. У грудні 2015 року, Fnatic перемогли NiP з рахунком 2-1 і забезпечили собі друге чемпіонство Fragbite Masters. Після перемоги на Fragbite Masters, Fnatic відновили першу позицію в рейтингу HLTV.org, а на сьогодні залишаються серед найкращих команд світу. Найкращий рік в історії Fnatic у CS:GO — це 2015. В цьому році Fnatic виграли 2 мейджори: ESL One Katowice 2015 і ESL One Cologne 2015. Також вони виграли ше щонайменше 6 великих турнірів. Усього понад 8 титулів за рік — абсолютне домінування на про-сцені. Легендарний склад Fnatic у 2015: JW (AWPer, зірка яскравих моментів), KRIMZ (сапорт, неймовірно стабільний гравець), flusha (ігровий мозок, майстер таймінгів), olofmeister (entry-фрагер і суперзірка) і pronax (капітан, стратег і тактик). olofmeister став гравецем №1 у світі у 2015 році (за версією HLTV)",
        players="fear - In-game Leader (IGL), Jambo - AWP-cнайпер (AWPer), blameF - Rifler, KRIMZ - Rifler, MATYS - Rifler, Independent - Головний тренер",
    )

    nip = Team(
        name="Ninjas in Pyjamas (NiP)",
        logo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHcY4qdJ1DJasWIehreygX0S2AW2yUZoFJ9Q&s",
        trophies=29,
        descr="Ninjas in Pyjamas (NiP) — легендарна кіберспортивна команда зі Швеції, заснована у 2000 році. NiP стала відомою завдяки домінуванню в Counter-Strike 1.6, а пізніше — в CS:GO. 2000–2007: NiP була однією з перших професійних CS-команд. У 2001 році виграла CPL World Championship. У 2005 році об’єдналась із SK Gaming, але пізніше знову відокремилась. 2012 – Ребрендинг та домінація в CS:GO: З виходом CS:GO NiP зібрала зірковий склад (f0rest, GeT_RiGhT, Xizt, friberg, Fifflaren), який встановив рекорд — 87 перемог поспіль на LAN-турнірах. У 2014 році команда стала віце-чемпіоном ESL One Cologne, а пізніше виграла ESL One Cologne 2014, свій перший CS:GO Major. 2015–2020: Період спадів і частих змін складу. Ключові гравці першого складу поступово залишили команду. Команда продовжувала виступати, але вже не мала такої домінантної позиції. 2021–дотепер: NiP провела ребілд, запросивши нових гравців, зокрема з інших країн, і активно працює над поверненням у топ. Команда прагне адаптуватися до сучасної сцени CS2. Команда відома своїм унікальним стилем гри та історичним внеском у розвиток сцени CS. Найкращим роком в історії Ninjas in Pyjamas (NiP) безсумнівно вважається 2013 рік. 87 перемог поспіль на LAN-турнірах — рекорд, який досі не побитий в історії CS:GO. У складі грали легенди сцени: GeT_RiGhT, f0rest, Xizt, friberg, Fifflaren. Також GeT_RiGhT був визнаний найкращим гравцем світу 2013 за версією HLTV.",
        players="Snappi - In‑Game Leader (IGL), sjuush - Rifler/Anchor, r1nkle - AWP-cнайпер (AWPer), ewjerkz - Rifler, arrozdoce - Rifler, Xizt - Головний тренер",
    )

    cloude9 = Team(
        name="Cloud9",
        logo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Cloud9_logo_c._2023.svg/800px-Cloud9_logo_c._2023.svg.png",
        trophies=5,
        descr="Cloud9 (C9) — американська кіберспортивна організація, заснована у 2013 році. Вона є однією з найвідоміших у Північній Америці та має довгу історію в CS:GO, а тепер і в CS2. 2014 — Cloud9 роблять свій вхід у CS:GO, підписавши склад compLexity, до якого входили популярні гравці NA, такі як shroud, n0thing, Hiko. 2018 рік — головний успіх: у січні C9 стали першими північноамериканцями, які виграли Major — ELEAGUE Boston 2018, перемігши FaZe у драматичному фіналі. Склад-переможець ELEAGUE Major 2018: tarik (IGL), Skadoodle (AWP), RUSH, autimatic і Stewie2K. Цей момент називають “Miracle in Boston” — comeback з 0‑2 у New Legends та перемоги над топ-командами. Після цього до 2020 року склад часто змінювався, але стабільних успіхів не було. Квітень 2022 — C9 повернулися в CS:GO, підписавши склад Gambit Esports (sh1ro, Ax1Le, interz, nafany, Hobbit) за ~1 млн. $. У червні 2022 вони виграли IEM Dallas 2022, перегравши ENCE з рахунком 3:0. Ax1Le став MVP турніру, а sh1ro та Ax1Le потрапили в топ‑20 HLTV 2022. Проте Major Antwerp 2022 — невдалий результат (12−14 місце). На IEM Rio Major 2022 C9 дійшли до Legends Stage, але поступилися MOUZ у чвертьфіналі. Січень 2023 — interz замінили на buster, у липні — прийшли electroNic і Perfecto, натомість пішли buster і nafany. Жовтень 2023 — пішли sh1ro, його замінив Boombl4. 2024 — успіх у PGL Copenhagen: проходять у плей-офф, але вилетіли у чвертьфіналі від Vitality. ElectroNic пішов у Virtus.pro, Perfecto та Hobbit — на лаву запасних. Липень 2024 — підписано HeavyGod, ICY і повернуто interz. Але до кінця року всі вони покинули команду — interz став вільним агентом, ICY перейшов у VP, HeavyGod — в G2, Boombl4 та Ax1Le — у BetBoom. 14 лютого 2025 Cloud9 офіційно оголосили про тимчасовий вихід з CS2: звільнено тренера groove та менеджера Sweetypotz, склад розпущений. Відтоді організація не має активного складу, хоча залишаються надії на можливе повернення. ",
        players="Стан - не має діючого складу",
    )

    astralis = Team(
        name="Astralis",
        logo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-OJLkEqLcAfe-znfg-8IpFkVh7h9pJ1JF6yuhzJok1dfsb54STHQkIcB3TBu010hqL5g&usqp=CAU",
        trophies=23,
        descr="Astralis — це професійна датська кіберспортивна команда, що спеціалізується на грі CS:GO. Вона була заснована у січні 2016 року, а її гравці швидко здобули визнання як одна з найсильніших і найтактичніших команд у світі. Колектив гравців, які раніше виступали у Team SoloMid (TSM), покинули організацію і створили власну команду — Astralis. 2016 рік: Команда тільки починає набирати форму, але вже показує сильні результати. 2017–2019 роки: Пік успіху Astralis. Вони виграли рекордні 4 турніри Major. Intel Grand Slam Season 1 (2018–2019): Astralis стала першою командою, яка виграла цю престижну нагороду, отримавши 1 000 000 доларів за серію перемог на великих турнірах. Найкращий рік для команди Astralis у CS:GO — це 2018. У 2018 році Astralis виграли два Major-турніри. Саме в 2018 році вони почали домінувати на світовій сцені, заклавши фундамент для подальших перемог, у тому числі виграшу Intel Grand Slam у 2018–2019. У 2018 команда показала неймовірну стабільність, тактичну глибину та майстерність, що зробило їх непереможними на багатьох змаганнях. Якщо говорити про сукупність досягнень, то 2018 і початок 2019 — це період, коли Astralis були на вершині своєї сили. Але саме 2018 вважають поворотним і найуспішнішим роком у їхній історії. Ось склад гравців Astralis у 2018 році: gla1ve, dev1ce, dupreeh, Xyp9x, Kjaerbye. У другій половині 2018 року Kjaerbye покинув Astralis, і на його місце прийшов Magisk , який став важливою частиною команди.",
        players="dev1ce - AWPer, Staehr - Rifler, stavn - Rifler/Opener, jabbi - Rifler, HooXi - In‑Game Leader (IGL), ruggah - Головний тренер",
    )
    mouz = Team(
        name="Mouz",
        logo_url="https://yt3.googleusercontent.com/iRY7jxVRvL3yDAgetgwroorXHCbEmaid_NFnwYVf9tpQVncwtNo5IyZvbprCKtg-iBKyBojT=s900-c-k-c0x00ffffff-no-rj",
        trophies=16,
        descr="mouz - одна з найвідоміших кіберспортивних організацій у Європі, особливо в дисципліні Counter-Strike. Вона була заснована в Німеччині у 2002 році і має багаторічну історію виступів у CS, включаючи версії 1.6, Source та нинішню — CS:GO / CS2.",
        players="torzsi - AWPer, xertioN - Entry Fragger / Rifler, Jimpphat - Rifler, siuhy - In‑Game Leader (IGL), Snappi - Support / Secondary Caller, sycrone - Coach",
    )
    gambit = Team(
        name="Gambit",
        logo_url="https://ru.csgo.com/thumb/team/size-team-logo-big/2018/09/23/MjNXS1MzNVp5N1dW.png",
        trophies=8,
        descr="Команда Gambit Esports — одна з найвідоміших кіберспортивних організацій у СНД-регіоні, яка здобула світове визнання в дисципліні Counter-Strike. Організація була заснована у Росії у 2013 році та брала участь у багатьох версіях CS, зокрема в CS:GO.",
        players="shobble - Coach, nafany - In‑Game Leader (IGL), sh1ro - AWPer, Ax1Le - Rifler, Hobbit - Support / Lurker, interz - Support",
    )
    vitality = Team(
        name="Vitality",
        logo_url="https://www.gamereactor.cn/media/35/teamvitalityhas_4133563.png",
        trophies=19,
        descr="це одна з найвідоміших кіберспортивних організацій у Франції та всій Європі, особливо в дисципліні Counter-Strike. Вона була заснована у 2013 році, але в CS:GO увійшла в 2018, одразу з амбіціями стати найкращими у світі.",
        players="ZywOo - AWPer, apEX - In‑Game Leader (IGL), Magisk - Rifler, dupreeh - Rifler, Spinx - Support, flameZ - Entry Fragger, XTQZZZ - Coach",
    )
    g2 = Team(
        name="G2",
        logo_url="https://counter-strike.de/wp-content/uploads/2023/11/G2-Esports.jpg",
        trophies=23,
        descr="дна з провідних кіберспортивних організацій у Європі, заснована у 2013 році з головним офісом у Франції. Відомі своєю агресивною та інноваційною грою в Counter-Strike, G2 швидко стали однією з найсильніших команд світу.",
        players="huNter - Rifler, nexa - In‑Game Leader (IGL), jackz - Rifler, AmaNEk - Support, m0NESY - AWPer, hAdji - Coach",
    )
    faze = Team(
        name="Faze",
        logo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Faze_Clan.svg/656px-Faze_Clan.svg.png",
        trophies=20,
        descr="Команда FaZe Clan — одна з найвідоміших і найпопулярніших кіберспортивних організацій у світі, заснована у 2016 році в Північній Америці. FaZe відома своїм зірковим складом, яскравим брендом і великим впливом не тільки у CS, а й у культурі кіберспорту загалом.",
        players="NiKo - Rifler, rain - Rifler, broky - AWPer, Twistzz - Rifler, karrigan - In‑Game Leader (IGL), ropz - Rifler, HS - Coach",
    )
    liquid = Team(
        name="Liquid",
        logo_url="https://de.egamersworld.com/uploads/counterstrike/teams/team-liquid-logo.webp",
        trophies=21,
        descr="Команда Team Liquid — одна з найвідоміших кіберспортивних організацій із Північної Америки, заснована у 2000 році. Вона має великий досвід у різних ігрових дисциплінах, а у CS:GO стала відомою завдяки стабільній грі на світовій сцені.",
        players="EliGE - Rifler, nitr0 - In‑Game Leader (IGL), NAF - Support / Rifler, Jerry - Entry Fragger, TACO - Support, zews - Coach",
    )
    virtus = Team(
        name="Virtus Pro",
        logo_url="https://images.seeklogo.com/logo-png/43/2/virtus-pro-logo-png_seeklogo-433313.png",
        trophies=21,
        descr="одна з найстаріших і найвідоміших кіберспортивних організацій СНД, заснована у 2003 році в Росії. Відомі своїм легендарним складом у CS 1.6 та пізніше в CS:GO, Virtus.pro були символом сили та стабільності на світовій сцені.",
        players="YEKINDAR - Entry Fragger, qikert - Rifler, Jame - AWPer, SANJI - Support, buster - In‑Game Leader (IGL), nkl - Coach",
    )
    simple = Player(
        name="Костилєв Олександр Олегович",
        nickname="s1mple",
        age=27,
        years="2013-:",
        photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Oleksandr_s1mple_Kostyliev.jpg/500px-Oleksandr_s1mple_Kostyliev.jpg",
        trophies=20,
        mvp=21,
        descr="Олександр Олегович Костилєв (нар. 2 жовтня 1997, Київ, Україна), більш відомий як s1mple — професійний український кіберспортсмен у дисципліні Counter-Strike. Найкращий гравець Counter-Strike: Global Offensive 2018, 2021 та 2022 років за версією порталу HLTV, вважається одним з найкращих гравців в історії Counter-Strike. У віці чотирьох років за рекомендацією старшого брата почав грати в Counter-Strike. У 2012 році придбав Counter-Strike: Global Offensive одразу після її виходу, а роком пізніше приєднався до своєї першої професійної команди. У 2021 році в складі команди Natus Vincere став переможцем і MVP PGL Major Stockholm 2021. У жовтні 2023 року оголосив про призупинення кар'єри професійного гравця. 5 травня 2025 року у NaVi повідомили, що Костилєв гратиме на правах оренди у складі американської команди FaZe Clan під час турнірів IEM Dallas 2025 та BLAST.tv Austin Major 2025, де замінить «broky», виведеного на лаву запасних. Вже 19 травня s1mple дебютував як найкращий гравець FaZe, але команда поступилася Team Liquid у верхній сітці групи В на старті IEM Dallas 2025. ",
    )
    dupreeh = Player(
        name="Пітер Ротманн Расмуссен",
        nickname="Dupreeh",
        age=32,
        years="2012-2025",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlHnuApy98E_BUMMdScELs7oGSzrXziGsiDA&s",
        trophies=32,
        mvp=2,
        descr="Петер «dupreeh» Расмуссен — данський професійний гравець в Counter-Strike: Global Offensive, який зараз грає за Heroic. Переможець п'ятьох мейджорів та три з яких було взято поспіль. dupreeh розпочав кар'єру у 2012 році, у складі 3DMAX . У січні 2013-го став під прапор Copenhagen Wolves , допоміг колективу зайняти 5-8 місце на DreamHack Winter 2013 . У грудні організація попрощалася з гравцями і вони продовжили спільні виступи під прапором über G33KZ. В 2014 році їх підписала організація Team Dignitas, де показали не погані результати. Січень 2015 року вони переходять до Team SoloMid,де виграють безліч турнірів, але самим великим досягненням було 4 місце на ESL One Cologne 2015. Після Team SoloMid вони де який час виступають під знаком питання (?), але потім засновують команду Astralis. У 2018 році увійшов до п'ятірки найкращих гравців світу за версією порталу HLTV.org. Він став MVP на ESL Pro League Season 7 та BLAST Pro Series: Global Final 2019. В 2022 році dupreeh разом із Magisk та їх тренером zonic, переходять до французької команди Team Vitality. Займають 2 місце на BLAST Premier Spring Final 2022. Потім перемагають на ESL Pro League Season 16. Після турніру став першим професійним гравцем, який досяг відмітку в $2.000.000, обігнавши своїх минулих одноклубників Xyp9x та device. Після того як вони кваліфікувалися на IEM Major Rio 2022 , він став першим хто був на всіх 18 мейджорах притому виграв 4 з них. В 2023 році команда Heroic підписує dupreeh до основного складу на заміну cadiaN. У планах менеджменту гравець повинен буде грати до кінця року. Dupreeh — один із найтитулованіших гравців в історії CS, який виграв 5 Major турнірів, понад 30 великих чемпіонатів і заробив понад $2 мільйони призових. ",
    )
    dev1ce = Player(
        name="Микола Редц",
        nickname="device",
        age=29,
        years="2011-:",
        photo_url="https://s2.glbimg.com/bQFA8xBgIwN-Q4EghEe53vMqfDY=/0x0:2048x1163/924x0/smart/filters:strip_icc()/s.glbimg.com/es/ge/f/original/2019/03/03/d0wtqvewoaqdnyt.jpg",
        trophies=31,
        mvp=19,
        descr="Device (справжнє ім’я — Ніколай Рідтц) — данський професійний гравець у Counter-Strike, один із найуспішніших в історії гри. Він почав кар’єру у 2011 році, а світову славу здобув у складі Team SoloMid та Astralis.Разом із братом у підлітковому віці почав грати у комп'ютерні ігри, зокрема, Counter-Strike: Source, але особливих успіхів не досяг. Незабаром після виходу Counter-Strike: Global Offensive почав активно її освоювати, домігшись того, що його почали запрошувати до кіберспортивних команд.До кіберспорту навчився добре грати в бадмінтон і, коли великі спортивні клуби Данії запропонували йому участь у змаганні під їх початком, Микола відхилив усі пропозиції, пославшись на травму коліна та бажання змагатися у кіберспорті. З Astralis device виграв 4 Major турніри, ставши ключовою фігурою в епосі домінування цієї команди. У 2021 році несподівано перейшов до Ninjas in Pyjamas, де провів понад рік. Після перерви у грі повернувся в 2023 році назад до Astralis. Device також входив до топ-5 гравців світу за версією HLTV п’ять років поспіль (2015–2019) та вважається одним із найстабільніших і найрозумніших AWP-гравців усіх часів.",
    )
    FalleN = Player(
        name="Габріель Толедо",
        nickname="FalleN",
        age=34,
        years="2014-:",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKDNwQy4gsOJtUwuLkCk9P8qmoSFXuqbLeXllYv_3dlpN7028iwt0O9TTpCWOS8P50IV8&usqp=CAU",
        trophies=13,
        mvp=4,
        descr="Габріель Толедо де Алькантара Сгуаріо (нар. 30 травня 1991), більш відомий як FalleN, - бразильський професійний гравець в Counter-Strike: Global Offensive , колишнім гравцем в Counter-Strike: Source і Counter-Strike 1. Наразі грає у команді FURIA на позиції снайпера. У 2015 році він був визнаний найвпливовішою людиною бразильського кіберспорту. Він також був номінований на премію eSports Industry Awards як особу року серед ПК-гравців у 2016 році. Є власником бразильської кіберспортивної організації Games Academy. У 2016 і 2017 роках FalleN був описаний як один із найкращих гравців AWP, ігрових лідерів та гравців загалом у світі. Він також є одним із небагатьох гравців у CS:GO , які поєднують роль снайпера та капітана. Gabriel «FalleN» Toledo розпочав свою професійну кар’єру в CS у 2014 році в команді Team KaBuM. Він швидко став одним із провідних бразильських гравців завдяки своїм лідерським якостям і видатній грі. У 2016 році FalleN здобув два Major-титули з командою Luminosity Gaming — ESL One Cologne і MLG Columbus, що зробило його легендою сцени. Пізніше він приєднався до SK Gaming, де продовжив здобувати важливі перемоги. Протягом кар’єри FalleN отримав кілька MVP-нагород за найкращі виступи на турнірах. Зараз він грає за FURIA Esports і продовжує залишатися впливовим гравцем у світі CS. ",
    )
    coldzera = Player(
        name="Марсело Аугусто Давид",
        nickname="coldzera",
        age=30,
        years="2014-:",
        photo_url="https://prosports.kz/storage/images/202403/206418_33680266e63df13bd7966b80ae97ffa9.jpg",
        trophies=20,
        mvp=8,
        descr="Марсело Аугусто Давид (нар. 31 жовтня 1994), більш відомий як coldzera - бразильський професійний гравець в Counter Strike: Global Offensive. На даний момент складається з організації RED Canids. Кіберспортивний ресурс HLTV називав coldzera найкращим гравцем у CS:GO за 2016 та 2017 роки. У серпні 2015 року coldzera підписав свій перший контракт із командою Luminosity Gaming. Його першим турніром за нову команду був ESL One Cologne 2015, де йому вдалося провести свою команду через груповий етап і вийти до чвертьфіналу турніру, але вони були вибиті шведською командою Fnatic. У 2016 році їм вдалося вийти з групового етапу у всіх турнірах, у яких вони брали участь, крім одного, включаючи два фінали. Однак лише у квітні вони змогли виграти свій перший турнір – MLG Columbus 2016. Це принесло команді 500 000 доларів призових, з яких 100 000 доларів отримав coldzera. Це був перший чемпіонат прем'єр-рівня, в якому бразилець отримав нагороду MVP (найцінніший гравець). Згодом його команда виграла ще два турніри за організацію Luminosity: DreamHack Austin та ESL Pro League Season 3. Останнім турніром команди став ECS Season 1, де вони посіли друге місце, поступившись команді G2 Esports. У липні 2016 року п'ять гравців, які грали за Luminosity Gaming, було викуплено організацією SK Gaming. Першим чемпіонатом команди став липневий ESL One Cologne 2016 всього через кілька днів після оголошення про придбання SK Gaming. Команді знову вдалося посісти перше місце; склад команди таким чином став дворазовим переможцем Major-чемпіонату: на той момент це вдалося лише шведській команді Fnatic та французькій Team EnVyUs. coldzera знову став MVP турніру. На тлі приголомшливих виступів, coldzera був визнаний найкращим гравцем HLTV у 2016 та 2017 роках. 23 червня 2018 року coldzera, Fer, FalleN, Stewie2K і Boltz підписали контракт з Made In Brazil. Склад команди був сформований незадовго до підписання контракту; і з новим складом команда виграє тільки один турнір - ZOTAC Cup Masters 2018. 21 грудня організація оголосила про повернення TACO, felps і zews. 20 найкращих гравців світу за версією HLTV. 12 липня 2019 року MIBR підтвердила, що coldzera стає запасним гравцем, а його місце тимчасово займає zews, який надалі виступив на StarLadder Berlin Major 2019. FaZe Clan стала перемога на BLAST Pro Series: Copenhagen 2019.",
    )
    kennyS = Player(
        name="Кенні Шраб",
        nickname="kennyS",
        age=30,
        years="2012-2023",
        photo_url="https://img-cdn.hltv.org/gallerypicture/jxZl_Xw8eUEnIiWbAnn4yZ.jpg?auto=compress&ixlib=java-2.1.0&q=75&w=800&s=bc85ad8d6febf706515aef2765427fc0",
        trophies=11,
        mvp=10,
        descr='Кенні Шраб (нар. 19 травня 1995 , Франція , Дінь-ле-Бен) - французький кіберспортсмен, відомий також під псевдонімом " kennyS ". У 2013 році займав 12 рядок у топ 20 гравців року за версією порталу HLTV.org, 6 місце у 2014 та 2015 роках. У 2016 році його результати дещо погіршилися, і він зайняв лише 13 рядок із 20. Чемпіон DreamHack Open Cluj-Napoca 2015. Кенні Шраб познайомився з Counter-Strike у 2009 році у 13-річному віці, це була Counter-Strike: Source версія. Він показував непогані результати і в 2011 році вирішив вирушити на турнір, де брали участь відомі французькі гравці, але після кількох матчів його забанили через підозру в читерстві, проте за нього став Вінсент « Happy » Сервоні, який не побачив жодного читерства, і Кенні продовжив грати далі на цьому чемпіонаті. Кенни «kennyS» Шруб розпочав свою професійну кар’єру у світі Counter-Strike у 2012 році, швидко зарекомендувавши себе як один із найкращих AWP-гравців завдяки винятковій швидкості реакції та точності. Його вміння володіти снайперською гвинтівкою зробило його одним із найнебезпечніших гравців на турнірній сцені, а його стиль гри викликав захоплення вболівальників по всьому світу. У 2015 році kennyS досяг найвищої точки своєї кар’єри, коли разом із командою Team EnVyUs здобув перемогу на престижному Major-турнірі DreamHack Open Cluj-Napoca. Ця перемога не лише принесла йому титул чемпіона світу, а й закріпила його статус однієї з найяскравіших зірок CS:GO. У подальші роки він виступав за такі відомі команди, як VeryGames, Titan, Team EnVyUs і G2 Esports, завдяки чому постійно залишався серед лідерів світового рейтингу. Протягом своєї кар’єри kennyS здобув понад 11 значних турнірних трофеїв, серед яких були перемоги на ESL Pro League, DreamHack Masters та інших великих подіях. Крім того, він отримав 10 MVP-нагород, які відзначали його видатні виступи та вплив на результат ігор. Його гра відзначалася не лише технікою, а й тактичною грамотністю, що робило його ключовим гравцем у будь-якій команді. У травні 2023 року kennyS офіційно оголосив про завершення своєї професійної кар’єри, завершивши еру одного з найяскравіших і найвпливовіших AWP-ерів у історії Counter-Strike. Його внесок у розвиток кіберспорту залишається незаперечним, а сама кар’єра надихає нове покоління гравців по всьому світу.',
    )
    NiKo = Player(
        name="Нікола Ковач",
        nickname="NiKo",
        age=28,
        years="2012-:",
        photo_url="https://s2-ge.glbimg.com/TgNrbvGpqyWS4xd2UoM62J_CeAs=/0x0:1600x1068/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2021/q/H/sQAbntRoKeDJNvF0zKdA/niko-major.jpg",
        trophies=17,
        mvp=9,
        descr="Нікола Ковач (босн.  Nikola Kovač , нар. 16 лютого 1997, Брчко) - боснійський кіберспортсмен з Counter-Strike 2, більш відомий під ніком « NiKo ». Нікола вперше отримав популярність у Європі після підписання контракту з організацією «iNation». Рівень гри Ковача викликав інтерес з боку mousesports, в яку він перейшов у березні 2015 року. У лютому 2017 року Нікола перейшов у FaZe Clan. Першу велику перемогу здобув на турнірі StarLadder StarSeries Season 3 , після чого пішов період без перемог протягом п'яти місяців, в результаті чого команда з працею потрапила на Esports Championship Series Season 3. GuardiaN » Ковач, команда здобула перемоги на ESL One: New York 2017 та ELEAGUE CS:GO Premier 2017. Після цього було два місяці без перемог, перш ніж вдалося завоювати трофей Esports Championship Series Season 4 в кінці року. Після поразки у фіналі на ELEAGUE Major: Boston 2018, знову була черга невдач, цього разу у складі з Річардом « Xizt » Ландстремом замість « olofmeister », поки їм не вдалося виграти IEM Sydney 2018, а невдовзі після цього, на початку літа. 2018 з Йоргеном «Cromen» Робертсеном як заміна. У жовтні 2018 року FaZe посіли перше місце на турнірі EPICENTER 2018 у Москві, що стало його сьомою перемогою у матчах за перше місце у головних турнірах з FaZe Clan. Наприкінці 2019 року кількість трофеїв зросла до десяти, оскільки FaZe виграла BLAST Pro Series Copenhagen. 2020 ознаменував ще одну перемогу для FaZe - вони виграли європейський дивізіон IEM New York 2020 Online, здобувши перемогу над OG Esports. 28 жовтня 2020 року, після трьох з половиною років співпраці з FaZe Clan, Ковач був придбаний організацією G2 Esports. Нікола Ковач з новою командою багато разів виводив G2 Esports у фінал різних турнірів, у тому числі і PGL Major Stockholm 2021 у якому вони програли команді Natus Vincere. 3 січня 2025 перейшов з G2 Esports в Falcons.",
    )
    Xyp9x = Player(
        name="Андреас Хейслет",
        nickname="Xyp9x",
        age=29,
        years="2011–2024",
        photo_url="https://esportenewsmundo.com.br/wp-content/uploads/2020/10/XYP9X-ASTRALIS.jpg",
        trophies=29,
        mvp=1,
        descr="Андреас Хейслет ( дат. Andreas Højsleth , нар. 11 вересня 1995, Орс, Данія ) — датський кіберспортсмен у дисципліні Counter-Strike: Global Offensive та Counter-Strike 2, більш відомий під ніком xyp9x. Є одним із найкращих гравців у клатч-ситуаціях (ситуацій «один проти одного або декількох суперників») на професійній сцені CS. Андреас разом з трьома співкомандниками ( dupreeh , gla1ve та dev1ce ) з Astralis стали першими, і єдиними гравцями, які виграли 4 мейджор-турніри з CS:GO, 3 з яких поспіль, що є абсолютними рекордами. За всю кар'єру Андреас заробив призовими понад 2 000 000 доларів США. У комп'ютерні ігри Андреас Хейслет почав грати з 9 років, поділяючи комп'ютер зі своїм старшим братом, завдяки якому Андреас і дізнався про Counter-Strike . Повертаючись зі школи, Xyp9x спостерігав за грою свого брата. У 14 років на подаровані гроші Андреас купив власний комп'ютер, щоб стати незалежним від свого старшого брата і мати можливість грати на вищому рівні. Свій нікнейм Андреас вигадав за допомогою випадкового натискання клавіш на клавіатурі. Андреас «Xyp9x» Хёйслет — легендарний данський гравець, який розпочав професійну кар’єру в Counter-Strike ще у 2011 році. З переходом на CS:GO у 2012-му він поступово зарекомендував себе як один із найрозумніших і найнадійніших гравців на сцені. Його фірмовим стилем стала неймовірна здатність вигравати клатчі (1vX-ситуації), за що він здобув прізвисько «клатч-майстер». Найвідоміший період його кар’єри припав на роки в команді Astralis, де разом із легендарним складом він виграв 4 Major-турніри (2017–2019) — рекордне досягнення у CS:GO — та став частиною домінантної ери, що включала перемогу в Intel Grand Slam Season 1. Його гра вирізнялася стабільністю, дисципліною й тактичною глибиною. Протягом кар’єри Xyp9x здобув приблизно 28–29 великих трофеїв, а також отримав одну MVP-нагороду — на турнірі IEM Katowice 2017, де показав виняткову гру. Він також входив у топ-гравців світу за версією HLTV у кількох сезонах. У 2024 році Xyp9x завершив свою активну ігрову кар’єру та приєднався до тренерського штабу MOUZ як асистент‑тренер, продовжуючи свій внесок у розвиток Counter-Strike уже за межами сервера.",
    )
    krimz = Player(
        name="Ларс Фредді Йоханссон",
        nickname="KRIMZ",
        age=31,
        years="2013–:",
        photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqqXG2Ae6vmLXc_MsQTvvmeUvNcVhfX6Hs8uzWD3oDgnH9_X8aIlVJnPSVFAcKjBscr4w&usqp=CAU",
        trophies=20,
        mvp=5,
        descr="Фредді «KRIMZ» Юганссон — шведський професійний гравець, який увійшов в історію Counter-Strike як один із найстабільніших та найнадійніших гравців свого покоління. Його кар’єра розпочалась у 2013 році, коли він дебютував на професійній сцені CS:GO. Уже за рік KRIMZ приєднався до легендарного складу Fnatic, разом з яким пережив період домінування у 2014–2015 роках. У складі Fnatic він виграв два Major-турніри — DreamHack Winter 2014 та ESL One Cologne 2015, що стало головним досягненням у його кар’єрі. Загалом KRIMZ здобув понад 20 трофеїв на великих LAN-турнірах і зарекомендував себе як опора команди — гравець, який завжди демонструє стабільну, спокійну й надзвичайно ефективну гру. Він також здобув 5 MVP-нагород, серед яких MVP ESWC 2014, DreamHack Open Tours 2015 та WESG 2017. Протягом більш ніж десяти років KRIMZ переважно представляв Fnatic, лише на короткий період відійшовши до GODSENT у 2016 році. Його стиль гри відзначався неймовірною дисципліною, ігровим інтелектом і здатністю вигравати клатчі без зайвого ризику. У 2025 році KRIMZ завершив свою професійну кар’єру, залишивши після себе велику спадщину як один із найуспішніших шведських гравців в історії CS:GO. Його ім’я назавжди пов’язане з епохою домінування Fnatic та золотим періодом класичного CS. ",
    )
    olof = Player(
        name="Олоф Кайбер Густаффсон",
        nickname="olofmeister",
        age=33,
        years="2010-2021",
        photo_url="https://isport.ua/i/18/47/20/3/1847203/image_main/7355589a3de36060bacb5fd1fb4473be-resize_crop_1Xquality_100Xallow_enlarge_0Xw_1200Xh_630.jpg",
        trophies=20,
        mvp=6,
        descr="Олоф «olofmeister» Кайб’єр Ґустафссон — шведський професійний гравець у CS:GO, який почав свою кар’єру приблизно у 2010 році, виступаючи за різні команди на національному рівні. З часом він привернув увагу своєю технічною майстерністю та гнучкістю у грі, що дозволило йому у 2013–2014 роках приєднатися до одного з найсильніших складів того часу — Fnatic. Саме з Fnatic olofmeister здобув світове визнання, ставши ключовою фігурою в період домінування команди на міжнародній сцені. У 2015 році разом із колективом він виграв два престижні Major-турніри — ESL One Katowice та ESL One Cologne, що стало кульмінацією його кар’єри. Окрім Major, він допоміг Fnatic здобути численні перемоги на інших великих LAN-турнірах, загалом маючи в активі понад 20 значних титулів. Олоф відзначався винятковою універсальністю: він міг грати на різних позиціях і виконувати найскладніші тактичні завдання, що зробило його незамінним гравцем у складі команди. Його ігровий стиль поєднував точність, розуміння ситуації та холоднокровність у критичних моментах, що неодноразово приносило йому MVP-нагороди — загалом шість разів він визнавався найкращим гравцем турніру. Попри серйозні травми, які вплинули на його кар’єру, olofmeister продовжував залишатися на високому рівні до 2021 року, коли офіційно завершив активну професійну гру. Після цього він залишився впливовою постаттю у світі кіберспорту, підтримуючи розвиток сцени і беручи участь у різних заходах, а також надихаючи нові покоління гравців. Його внесок у Counter-Strike залишається одним із найзначніших в історії гри.",
    )
    with Session() as conn:
        conn.add(user_admin)
        conn.add(navi)
        conn.add(fnatic)
        conn.add(nip)
        conn.add(cloude9)
        conn.add(astralis)
        conn.add(mouz)
        conn.add(gambit)
        conn.add(vitality)
        conn.add(g2)
        conn.add(faze)
        conn.add(liquid)
        conn.add(virtus)
        conn.add(simple)
        conn.add(dupreeh)
        conn.add(dev1ce)
        conn.add(FalleN)
        conn.add(coldzera)
        conn.add(kennyS)
        conn.add(NiKo)
        conn.add(Xyp9x)
        conn.add(krimz)
        conn.add(olof)
        conn.commit()


if __name__ == "__main__":
    init_db()
