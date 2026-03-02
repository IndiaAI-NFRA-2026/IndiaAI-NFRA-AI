RULES_DB = {
    "IND_AS_1": {
    "version": "1.1.0",
    "description": "Compliance rules for Indian Accounting Standard (Ind AS) 1: Presentation of Financial Statements.",
    "rules": [
    {
        "rule_id": "INDAS1-01",
        "description": "Present a complete set of financial statements including Balance Sheet, Statement of Profit and Loss, Statement of Changes in Equity, Statement of Cash Flows, and Notes.",
        "mapped_paragraphs": "10",
        "type": "Structural",
        "full_text": "A complete set of financial statements comprises: (a) a balance sheet as at the end of the period; (b) a statement of profit and loss for the period; (c) Statement of changes in equity for the period; (d) a statement of cash flows for the period; (e) notes, comprising material accounting policy information and other explanatory information; (ea) comparative information in respect of the preceding period as specified in paragraphs 38 and 38A; and (f) a balance sheet as at the beginning of the preceding period when an entity applies an accounting policy retrospectively or makes a retrospective restatement of items in its financial statements, or when it reclassifies items in its financial statements in accordance with paragraphs 40A–40D."
    },
    {
        "rule_id": "INDAS1-02",
        "description": "Present a single Statement of Profit and Loss with two sections: Profit or Loss first, followed by Other Comprehensive Income.",
        "mapped_paragraphs": "10A",
        "type": "Structural",
        "full_text": "An entity shall present a single statement of profit and loss, with profit or loss and other comprehensive income presented in two sections. The sections shall be presented together, with the profit or loss section presented first followed directly by the other comprehensive income section."
    },
    {
        "rule_id": "INDAS1-03",
        "description": "Include an explicit and unreserved statement of compliance with Ind AS in the notes.",
        "mapped_paragraphs": "16",
        "type": "Disclosure",
        "full_text": "An entity whose financial statements comply with Ind ASs shall make an explicit and unreserved statement of such compliance in the notes. An entity shall not describe financial statements as complying with Ind ASs unless they comply with all the requirements of Ind ASs."
    },
    {
        "rule_id": "INDAS1-04",
        "description": "Prepare financial statements on a going concern basis unless management intends to liquidate or cease trading; disclose material uncertainties if they exist.",
        "mapped_paragraphs": "25",
        "type": "Disclosure",
        "full_text": "An entity shall prepare financial statements on a going concern basis unless management either intends to liquidate the entity or to cease trading, or has no realistic alternative but to do so. When management is aware, in making its assessment, of material uncertainties related to events or conditions that may cast significant doubt upon the entity’s ability to continue as a going concern, the entity shall disclose those uncertainties. When an entity does not prepare financial statements on a going concern basis, it shall disclose that fact, together with the basis on which it prepared the financial statements and the reason why the entity is not regarded as a going concern."
    },
    {
        "rule_id": "INDAS1-05",
        "description": "Prepare financial statements (except Cash Flow) using the accrual basis of accounting.",
        "mapped_paragraphs": "27",
        "type": "Structural",
        "full_text": "An entity shall prepare its financial statements, except for cash flow information, using the accrual basis of accounting."
    },
    {
        "rule_id": "INDAS1-06",
        "description": "Present separately each material class of similar items; present dissimilar items separately unless immaterial.",
        "mapped_paragraphs": "29",
        "type": "Structural",
        "full_text": "An entity shall present separately each material class of similar items. An entity shall present separately items of a dissimilar nature or function unless they are immaterial except when required by law."
    },
    {
        "rule_id": "INDAS1-07",
        "description": "Do not offset assets and liabilities or income and expenses unless required or permitted by an Ind AS.",
        "mapped_paragraphs": "32",
        "type": "Numerical",
        "full_text": "An entity shall not offset assets and liabilities or income and expenses, unless required or permitted by an Ind AS."
    },
    {
        "rule_id": "INDAS1-08",
        "description": "Present a complete set of financial statements at least annually; disclose reasons if reporting period changes.",
        "mapped_paragraphs": "36",
        "type": "Structural",
        "full_text": "An entity shall present a complete set of financial statements (including comparative information) at least annually. When an entity changes the end of its reporting period and presents financial statements for a period longer or shorter than one year, an entity shall disclose, in addition to the period covered by the financial statements: (a) the reason for using a longer or shorter period, and (b) the fact that amounts presented in the financial statements are not entirely comparable."
    },
    {
        "rule_id": "INDAS1-09",
        "description": "Present comparative information for the preceding period for all amounts reported in the current period.",
        "mapped_paragraphs": "38",
        "type": "Numerical",
        "full_text": "Except when Ind ASs permit or require otherwise, an entity shall present comparative information in respect of the preceding period for all amounts reported in the current period’s financial statements. An entity shall include comparative information for narrative and descriptive information if it is relevant to understanding the current period’s financial statements."
    },
    {
        "rule_id": "INDAS1-10",
        "description": "Present a third balance sheet (at the beginning of the preceding period) if applying an accounting policy retrospectively or making a retrospective restatement that has a material effect.",
        "mapped_paragraphs": "40A",
        "type": "Structural",
        "full_text": "An entity shall present a third balance sheet as at the beginning of the preceding period in addition to the minimum comparative financial statements required in paragraph 38A if: (a) it applies an accounting policy retrospectively, makes a retrospective restatement of items in its financial statements or reclassifies items in its financial statements; and (b) the retrospective application, retrospective restatement or the reclassification has a material effect on the information in the balance sheet at the beginning of the preceding period."
    },
    {
        "rule_id": "INDAS1-11",
        "description": "Clearly identify the financial statements, reporting currency, and level of rounding.",
        "mapped_paragraphs": "49–51",
        "type": "Disclosure",
        "full_text": "An entity shall clearly identify the financial statements and distinguish them from other information in the same published document... An entity shall clearly identify each financial statement and the notes... (a) the name of the reporting entity...; (b) whether the financial statements are of an individual entity or a group of entities; (c) the date of the end of the reporting period...; (d) the presentation currency...; and (e) the level of rounding used in presenting amounts in the financial statements."
    },
    {
        "rule_id": "INDAS1-12",
        "description": "Include minimum line items in the Balance Sheet (e.g., PPE, Intangible Assets, Financial Assets, Inventories, Trade Receivables, Cash, Trade Payables, Provisions).",
        "mapped_paragraphs": "54",
        "type": "Structural",
        "full_text": "The balance sheet shall include line items that present the following amounts: (a) property, plant and equipment; (b) investment property; (c) intangible assets; (d) financial assets...; (da) portfolios of contracts within the scope of Ind AS 117...; (e) investments accounted for using the equity method; (f) biological assets...; (g) inventories; (h) trade and other receivables; (i) cash and cash equivalents; (j) the total of assets classified as held for sale...; (k) trade and other payables; (l) provisions; (m) financial liabilities...; (ma) portfolios of contracts within the scope of Ind AS 117 that are liabilities...; (n) liabilities and assets for current tax...; (o) deferred tax liabilities and deferred tax assets...; (p) liabilities included in disposal groups classified as held for sale...; (q) non-controlling interests, presented within equity; and (r) issued capital and reserves attributable to owners of the parent."
    },
    {
        "rule_id": "INDAS1-13",
        "description": "Present Current and Non-current assets and liabilities as separate classifications (unless liquidity presentation is more reliable).",
        "mapped_paragraphs": "60",
        "type": "Structural",
        "full_text": "An entity shall present current and non-current assets, and current and non-current liabilities, as separate classifications in its balance sheet in accordance with paragraphs 66–76 except when a presentation based on liquidity provides information that is reliable and more relevant. When that exception applies, an entity shall present all assets and liabilities in order of liquidity."
    },
    {
        "rule_id": "INDAS1-14",
        "description": "Classify an asset as current if realized in the normal operating cycle, held for trading, or realized within 12 months.",
        "mapped_paragraphs": "66",
        "type": "Structural",
        "full_text": "An entity shall classify an asset as current when: (a) it expects to realise the asset, or intends to sell or consume it, in its normal operating cycle; (b) it holds the asset primarily for the purpose of trading; (c) it expects to realise the asset within twelve months after the reporting period; or (d) the asset is cash or a cash equivalent... unless the asset is restricted from being exchanged or used to settle a liability for at least twelve months after the reporting period. An entity shall classify all other assets as non-current."
    },
    {
        "rule_id": "INDAS1-15",
        "description": "Classify a liability as current if settled in normal operating cycle, held for trading, due within 12 months, or if there is no unconditional right to defer settlement for 12 months.",
        "mapped_paragraphs": "69",
        "type": "Structural",
        "full_text": "An entity shall classify a liability as current when: (a) it expects to settle the liability in its normal operating cycle; (b) it holds the liability primarily for the purpose of trading; (c) the liability is due to be settled within twelve months after the reporting period; or (d) it does not have an unconditional right to defer settlement of the liability for at least twelve months after the reporting period... An entity shall classify all other liabilities as non-current."
    },
    {
        "rule_id": "INDAS1-16",
        "description": "Classify liabilities and disclose covenants risks at the end of the reporting period.",
        "mapped_paragraphs": "72B, 74–76ZA",
        "type": "Structural",
        "full_text": "An entity’s right to defer settlement of a liability arising from a loan arrangement for at least twelve months after the reporting period may be subject to the entity complying with conditions specified in that loan arrangement... Where there is a breach of a material covenant... the entity does not classify the liability as current, if the lender agreed, after the reporting period and before the approval of the financial statements for issue, not to demand payment... In applying paragraphs 69–75, an entity might classify liabilities arising from loan arrangements as non-current when the entity’s right to defer settlement... is subject to the entity complying with covenants within twelve months... In such situations, the entity shall disclose information in the notes that enables users of financial statements to understand the risk..."
    },
    {
        "rule_id": "INDAS1-17",
        "description": "Disclose share capital details: authorized, issued, par value, and reconciliation of shares at beginning/end of period.",
        "mapped_paragraphs": "79",
        "type": "Numerical",
        "full_text": "An entity shall disclose the following...: (a) for each class of share capital: (i) the number of shares authorised; (ii) the number of shares issued and fully paid, and issued but not fully paid; (iii) par value per share...; (iv) a reconciliation of the number of shares outstanding at the beginning and at the end of the period; (v) the rights, preferences and restrictions attaching to that class...; (vi) shares in the entity held by the entity or by its subsidiaries or associates; and (vii) shares reserved for issue under options and contracts...; and (b) a description of the nature and purpose of each reserve within equity."
    },
    {
        "rule_id": "INDAS1-18",
        "description": "Present Total Comprehensive Income, allocating amounts attributable to owners of the parent and non-controlling interests.",
        "mapped_paragraphs": "81A–81B",
        "type": "Numerical",
        "full_text": "The statement of profit and loss shall present...: (a) profit or loss; (b) total other comprehensive income; (c) comprehensive income for the period... An entity shall present...: (a) profit or loss for the period attributable to: (i) non-controlling interests, and (ii) owners of the parent. (b) comprehensive income for the period attributable to: (i) non-controlling interests, and (ii) owners of the parent."
    },
    {
        "rule_id": "INDAS1-19",
        "description": "Include minimum line items in Profit or Loss section (Revenue, Finance costs, Tax expense, etc.).",
        "mapped_paragraphs": "82",
        "type": "Numerical",
        "full_text": "The profit or loss section of the statement of profit and loss shall include line items that present the following amounts for the period: (a) revenue...; (aa) gains and losses arising from the derecognition of financial assets measured at amortised cost; (ab) insurance service expenses...; (ac) income or expenses from reinsurance contracts...; (b) finance costs; (ba) impairment losses...; (bb) insurance finance income or expenses...; (bc) finance income or expenses from reinsurance contracts held; (c) share of the profit or loss of associates and joint ventures...; (ca) if a financial asset is reclassified out of the amortised cost measurement category...; (cb) if a financial asset is reclassified out of the fair value through other comprehensive income...; (d) tax expense; (ea) a single amount for the total of discontinued operations."
    },
    {
        "rule_id": "INDAS1-20",
        "description": "Group Other Comprehensive Income (OCI) items into those that will not be reclassified to profit or loss and those that will be.",
        "mapped_paragraphs": "82A",
        "type": "Structural",
        "full_text": "The other comprehensive income section shall present line items for the amounts for the period of: (a) items of other comprehensive income... classified by nature and grouped into those that...: (i) will not be reclassified subsequently to profit or loss; and (ii) will be reclassified subsequently to profit or loss when specific conditions are met."
    },
    {
        "rule_id": "INDAS1-21",
        "description": "Do not present any items of income or expense as 'extraordinary items'.",
        "mapped_paragraphs": "87",
        "type": "Structural",
        "full_text": "An entity shall not present any items of income or expense as extraordinary items, in the statement of profit and loss or in the notes."
    },
    {
        "rule_id": "INDAS1-22",
        "description": "Present analysis of expenses recognized in profit or loss using the 'nature of expense' method.",
        "mapped_paragraphs": "99",
        "type": "Structural",
        "full_text": "An entity shall present an analysis of expenses recognised in profit or loss using a classification based on the nature of expense method."
    },
    {
        "rule_id": "INDAS1-23",
        "description": "Present a Statement of Changes in Equity showing total comprehensive income, retrospective adjustments, and reconciliation of carrying amounts.",
        "mapped_paragraphs": "106",
        "type": "Numerical",
        "full_text": "An entity shall present a statement of changes in equity... The statement of changes in equity includes the following information: (a) total comprehensive income for the period...; (b) for each component of equity, the effects of retrospective application or retrospective restatement...; (d) for each component of equity, a reconciliation between the carrying amount at the beginning and the end of the period, separately... disclosing changes resulting from: (i) profit or loss; (ii) other comprehensive income; (iii) transactions with owners...; and (iv) any item recognised directly in equity..."
    },
    {
        "rule_id": "INDAS1-24",
        "description": "Disclose dividends recognized as distributions and related amount per share.",
        "mapped_paragraphs": "107",
        "type": "Disclosure",
        "full_text": "An entity shall present, either in the statement of changes in equity or in the notes, the amount of dividends recognised as distributions to owners during the period, and the related amount of dividends per share."
    },
    {
        "rule_id": "INDAS1-25",
        "description": "Present notes in a systematic manner and cross-reference them to the main financial statements.",
        "mapped_paragraphs": "113",
        "type": "Structural",
        "full_text": "An entity shall present notes in a systematic manner. In determining a systematic manner, the entity shall consider the effect on the understandability and comparability of its financial statements. An entity shall cross-reference each item in the balance sheet and in the statement of profit and loss, and in the statements of changes in equity and of cash flows to any related information in the notes."
    },
    {
        "rule_id": "INDAS1-26",
        "description": "Disclose material accounting policy information.",
        "mapped_paragraphs": "117",
        "type": "Disclosure",
        "full_text": "An entity shall disclose material accounting policy information (see paragraph 7). Accounting policy information is material if, when considered together with other information included in an entity’s financial statements, it can reasonably be expected to influence decisions that the primary users of general purpose financial statements make on the basis of those financial statements."
    },
    {
        "rule_id": "INDAS1-27",
        "description": "Disclose judgements (apart from estimations) that management has made that have the most significant effect on recognized amounts.",
        "mapped_paragraphs": "122",
        "type": "Disclosure",
        "full_text": "An entity shall disclose, along with material accounting policy information or other notes, the judgements, apart from those involving estimations (see paragraph 125), that management has made in the process of applying the entity’s accounting policies and that have the most significant effect on the amounts recognised in the financial statements."
    },
    {
        "rule_id": "INDAS1-28",
        "description": "Disclose assumptions and major sources of estimation uncertainty that have a significant risk of resulting in material adjustments.",
        "mapped_paragraphs": "125",
        "type": "Disclosure",
        "full_text": "An entity shall disclose information about the assumptions it makes about the future, and other major sources of estimation uncertainty at the end of the reporting period, that have a significant risk of resulting in a material adjustment to the carrying amounts of assets and liabilities within the next financial year. In respect of those assets and liabilities, the notes shall include details of: (a) their nature, and (b) their carrying amount as at the end of the reporting period."
    },
    {
        "rule_id": "INDAS1-29",
        "description": "Disclose qualitative and quantitative information about objectives, policies, and processes for managing capital.",
        "mapped_paragraphs": "134–135",
        "type": "Disclosure",
        "full_text": "An entity shall disclose information that enables users of its financial statements to evaluate the entity’s objectives, policies and processes for managing capital. To comply with paragraph 134, the entity discloses the following: (a) qualitative information about its objectives, policies and processes for managing capital... (b) summary quantitative data about what it manages as capital... (c) any changes in (a) and (b) from the previous period. (d) whether during the period it complied with any externally imposed capital requirements... (e) when the entity has not complied... the consequences of such non-compliance."
    },
    {
        "rule_id": "INDAS1-30",
        "description": "Disclose proposed dividends declared after the reporting period but before approval of financial statements.",
        "mapped_paragraphs": "137",
        "type": "Disclosure",
        "full_text": "An entity shall disclose in the notes: (a) the amount of dividends proposed or declared before the financial statements were approved for issue but not recognised as a distribution to owners during the period, and the related amount per share; and (b) the amount of any cumulative preference dividends not recognised."
    },
    {
        "rule_id": "INDAS1-31",
        "description": "Disclose the domicile and legal form of the entity, its country of incorporation, registered office address, nature of operations, and name of the parent entity.",
        "mapped_paragraphs": "138",
        "type": "Disclosure",
        "full_text": "An entity shall disclose the following, if not disclosed elsewhere in information published with the financial statements: (a) the domicile and legal form of the entity, its country of incorporation and the address of its registered office...; (b) a description of the nature of the entity’s operations and its principal activities; (c) the name of the parent and the ultimate parent of the group; and (d) if it is a limited life entity, information regarding the length of its life."
    },
    {
        "rule_id": "INDAS1-32",
        "description": "Retain presentation and classification of items from one period to the next (Consistency).",
        "mapped_paragraphs": "45",
        "type": "Structural",
        "full_text": "An entity shall retain the presentation and classification of items in the financial statements from one period to the next unless: (a) it is apparent, following a significant change in the nature of the entity’s operations or a review of its financial statements, that another presentation or classification would be more appropriate...; or (b) an Ind AS requires a change in presentation."
    }
  ]
},
    "IND_AS_7": {
    "version": "1.0.0",
    "description": "Compliance rules for Indian Accounting Standard (Ind AS) 7: Statement of Cash Flows.",
    "rules": [
    {
        "rule_id": "INDAS7-01",
        "description": "Prepare a statement of cash flows and present it as an integral part of the financial statements for each period presented.",
        "mapped_paragraphs": "1",
        "type": "Structural",
        "full_text": "An entity shall prepare a statement of cash flows in accordance with the requirements of this Standard and shall present it as an integral part of its financial statements for each period for which financial statements are presented."
    },
    {
        "rule_id": "INDAS7-02",
        "description": "Classify cash flows during the period into operating, investing, and financing activities.",
        "mapped_paragraphs": "10",
        "type": "Structural",
        "full_text": "The statement of cash flows shall report cash flows during the period classified by operating, investing and financing activities."
    },
    {
        "rule_id": "INDAS7-03",
        "description": "Report cash flows from operating activities using either the direct method or the indirect method.",
        "mapped_paragraphs": "18",
        "type": "Structural",
        "full_text": "An entity shall report cash flows from operating activities using either: (a) the direct method, whereby major classes of gross cash receipts and gross cash payments are disclosed; or (b) the indirect method, whereby profit or loss is adjusted for the effects of transactions of a noncash nature, any deferrals or accruals of past or future operating cash receipts or payments, and items of income or expense associated with investing or financing cash flows."
    },
    {
        "rule_id": "INDAS7-04",
        "description": "Report separately major classes of gross cash receipts and gross cash payments for investing and financing activities (unless netting criteria are met).",
        "mapped_paragraphs": "21",
        "type": "Structural",
        "full_text": "An entity shall report separately major classes of gross cash receipts and gross cash payments arising from investing and financing activities, except to the extent that cash flows described in paragraphs 22 and 24 are reported on a net basis."
    },
    {
        "rule_id": "INDAS7-05",
        "description": "Report on a net basis only for: (a) customers' behalf, (b) items with quick turnover/large amount/short maturity, or (c) specific financial institution activities.",
        "mapped_paragraphs": "22–24",
        "type": "Structural",
        "full_text": "Cash flows arising from the following operating, investing or financing activities may be reported on a net basis: (a) cash receipts and payments on behalf of customers when the cash flows reflect the activities of the customer rather than those of the entity; and (b) cash receipts and payments for items in which the turnover is quick, the amounts are large, and the maturities are short... Cash flows arising from each of the following activities of a financial institution may be reported on a net basis..."
    },
    {
        "rule_id": "INDAS7-06",
        "description": "Record foreign currency cash flows at the exchange rate at the date of the cash flow (or a weighted average approximation).",
        "mapped_paragraphs": "25–27",
        "type": "Numerical",
        "full_text": "Cash flows arising from transactions in a foreign currency shall be recorded in an entity’s functional currency by applying to the foreign currency amount the exchange rate between the functional currency and the foreign currency at the date of the cash flow. The cash flows of a foreign subsidiary shall be translated at the exchange rates between the functional currency and the foreign currency at the dates of the cash flows. Cash flows denominated in a foreign currency are reported in a manner consistent with Ind AS 21..."
    },
    {
        "rule_id": "INDAS7-07",
        "description": "Exclude unrealized foreign exchange gains and losses from cash flows; present them separately to reconcile opening and closing cash balances.",
        "mapped_paragraphs": "28",
        "type": "Numerical",
        "full_text": "Unrealised gains and losses arising from changes in foreign currency exchange rates are not cash flows. However, the effect of exchange rate changes on cash and cash equivalents held or due in a foreign currency is reported in the statement of cash flows in order to reconcile cash and cash equivalents at the beginning and the end of the period. This amount is presented separately from cash flows from operating, investing and financing activities and includes the differences, if any, had those cash flows been reported at end of period exchange rates."
    },
    {
        "rule_id": "INDAS7-08",
        "description": "For non-financial entities: Classify interest paid as Financing, interest and dividends received as Investing, and dividends paid as Financing.",
        "mapped_paragraphs": "31",
        "type": "Structural",
        "full_text": "Cash flows from interest and dividends received and paid shall each be disclosed separately... In the case of other entities, cash flows arising from interest paid should be classified as cash flows from financing activities while interest and dividends received should be classified as cash flows from investing activities. Dividends paid should be classified as cash flows from financing activities."
    },
    {
        "rule_id": "INDAS7-09",
        "description": "For financial institutions: Classify interest paid and interest and dividends received as Operating activities.",
        "mapped_paragraphs": "31",
        "type": "Structural",
        "full_text": "Cash flows arising from interest paid and interest and dividends received in the case of a financial institution should be classified as cash flows arising from operating activities."
    },
    {
        "rule_id": "INDAS7-10",
        "description": "Disclose total interest paid, whether expensed in profit or loss or capitalized.",
        "mapped_paragraphs": "32",
        "type": "Disclosure",
        "full_text": "The total amount of interest paid during a period is disclosed in the statement of cash flows whether it has been recognised as an expense in profit or loss or capitalised in accordance with Ind AS 23, Borrowing Costs."
    },
    {
        "rule_id": "INDAS7-11",
        "description": "Disclose cash flows from income taxes separately and classify as operating unless specifically identified with investing or financing.",
        "mapped_paragraphs": "35",
        "type": "Structural",
        "full_text": "Cash flows arising from taxes on income shall be separately disclosed and shall be classified as cash flows from operating activities unless they can be specifically identified with financing and investing activities."
    },
    {
        "rule_id": "INDAS7-12",
        "description": "Restrict reporting of cash flows from equity/cost method investments (associates/subsidiaries) to actual cash flows between investor and investee.",
        "mapped_paragraphs": "37",
        "type": "Numerical",
        "full_text": "When accounting for an investment in an associate, a joint venture or a subsidiary accounted for by use of the equity or cost method, an investor restricts its reporting in the statement of cash flows to the cash flows between itself and the investee, for example, to dividends and advances."
    },
    {
        "rule_id": "INDAS7-13",
        "description": "Present aggregate cash flows arising from obtaining or losing control of subsidiaries separately and classify as investing activities.",
        "mapped_paragraphs": "39",
        "type": "Structural",
        "full_text": "The aggregate cash flows arising from obtaining or losing control of subsidiaries or other businesses shall be presented separately and classified as investing activities."
    },
    {
        "rule_id": "INDAS7-14",
        "description": "Disclose details of obtaining/losing control: consideration paid/received, portion in cash, and amount of cash/assets/liabilities in the subsidiary.",
        "mapped_paragraphs": "40",
        "type": "Disclosure",
        "full_text": "An entity shall disclose, in aggregate, in respect of both obtaining and losing control of subsidiaries or other businesses during the period each of the following: (a) the total consideration paid or received; (b) the portion of the consideration consisting of cash and cash equivalents; (c) the amount of cash and cash equivalents in the subsidiaries...; and (d) the amount of the assets and liabilities other than cash or cash equivalents in the subsidiaries or other businesses over which control is obtained or lost..."
    },
    {
        "rule_id": "INDAS7-15",
        "description": "Classify cash flows from changes in ownership interests in a subsidiary that do not result in a loss of control as financing activities.",
        "mapped_paragraphs": "42A",
        "type": "Structural",
        "full_text": "Cash flows arising from changes in ownership interests in a subsidiary that do not result in a loss of control shall be classified as cash flows from financing activities , unless the subsidiary is held by an investment entity..."
    },
    {
        "rule_id": "INDAS7-16",
        "description": "Exclude non-cash investing and financing transactions (e.g., debt to equity conversion) from the statement of cash flows; disclose elsewhere.",
        "mapped_paragraphs": "43",
        "type": "Disclosure",
        "full_text": "Investing and financing transactions that do not require the use of cash or cash equivalents shall be excluded from a statement of cash flows. Such transactions shall be disclosed elsewhere in the financial statements in a way that provides all the relevant information about these investing and financing activities."
    },
    {
        "rule_id": "INDAS7-17",
        "description": "Disclose changes in liabilities arising from financing activities, distinguishing between cash changes and non-cash changes (e.g., FX, fair value).",
        "mapped_paragraphs": "44A–44B",
        "type": "Disclosure",
        "full_text": "An entity shall provide disclosures that enable users of financial statements to evaluate changes in liabilities arising from financing activities, including both changes arising from cash flows and non-cash changes. To the extent necessary... an entity shall disclose the following changes...: (a) changes from financing cash flows; (b) changes arising from obtaining or losing control...; (c) the effect of changes in foreign exchange rates; (d) changes in fair values; and (e) other changes."
    },
    {
        "rule_id": "INDAS7-18",
        "description": "Disclose aggregate information about supplier finance arrangements: terms, carrying amounts, and payment due date ranges.",
        "mapped_paragraphs": "44H",
        "type": "Disclosure",
        "full_text": "To meet the objectives in paragraph 44F, an entity shall disclose in aggregate for its supplier finance arrangements: (a) the terms and conditions... (b) as at the beginning and end of the reporting period: (i) the carrying amounts... (ii) the carrying amounts... for which suppliers have already received payment... (iii) the range of payment due dates..."
    },
    {
        "rule_id": "INDAS7-19",
        "description": "Disclose components of cash and cash equivalents and present a reconciliation to the amounts reported in the balance sheet.",
        "mapped_paragraphs": "45",
        "type": "Disclosure",
        "full_text": "An entity shall disclose the components of cash and cash equivalents and shall present a reconciliation of the amounts in its statement of cash flows with the equivalent items reported in the balance sheet."
    },
    {
        "rule_id": "INDAS7-20",
        "description": "Disclose the policy adopted in determining the composition of cash and cash equivalents.",
        "mapped_paragraphs": "46",
        "type": "Disclosure",
        "full_text": "In view of the variety of cash management practices and banking arrangements around the world and in order to comply with Ind AS 1... an entity discloses the policy which it adopts in determining the composition of cash and cash equivalents."
    },
    {
        "rule_id": "INDAS7-21",
        "description": "Disclose significant cash and cash equivalent balances held by the entity that are not available for use by the group (with management commentary).",
        "mapped_paragraphs": "48",
        "type": "Disclosure",
        "full_text": "An entity shall disclose, together with a commentary by management, the amount of significant cash and cash equivalent balances held by the entity that are not available for use by the group."
    }
  ]
},
    "IND_AS_115": {
    "version": "1.0.0",
    "description": "Compliance rules for Indian Accounting Standard (Ind AS) 115: Revenue from Contracts with Customers.",
    "rules": [
    {
        "rule_id": "INDAS115-01",
        "description": "Recognize revenue to depict the transfer of promised goods or services to customers in an amount reflecting the consideration expected.",
        "mapped_paragraphs": "2",
        "type": "Structural",
        "full_text": "The core principle of this Standard is that an entity shall recognise revenue to depict the transfer of promised goods or services to customers in an amount that reflects the consideration to which the entity expects to be entitled in exchange for those goods or services."
    },
    {
        "rule_id": "INDAS115-02",
        "description": "Account for a contract only when all 5 criteria are met: approval, identified rights, identified payment terms, commercial substance, and probable collection.",
        "mapped_paragraphs": "9",
        "type": "Structural",
        "full_text": "An entity shall account for a contract with a customer that is within the scope of this Standard only when all of the following criteria are met: (a) the parties to the contract have approved the contract...; (b) the entity can identify each party’s rights regarding the goods or services to be transferred; (c) the entity can identify the payment terms for the goods or services to be transferred; (d) the contract has commercial substance...; and (e) it is probable that the entity will collect the consideration to which it will be entitled..."
    },
    {
        "rule_id": "INDAS115-03",
        "description": "Combine contracts entered into at/near the same time with the same customer if negotiated as a package, linked price, or single performance obligation.",
        "mapped_paragraphs": "17",
        "type": "Structural",
        "full_text": "An entity shall combine two or more contracts entered into at or near the same time with the same customer (or related parties of the customer) and account for the contracts as a single contract if one or more of the following criteria are met: (a) the contracts are negotiated as a package with a single commercial objective; (b) the amount of consideration to be paid in one contract depends on the price or performance of the other contract; or (c) the goods or services promised in the contracts... are a single performance obligation..."
    },
    {
        "rule_id": "INDAS115-04",
        "description": "Identify distinct goods or services (or a series of distinct goods/services) as separate performance obligations.",
        "mapped_paragraphs": "22",
        "type": "Structural",
        "full_text": "At contract inception, an entity shall assess the goods or services promised in a contract with a customer and shall identify as a performance obligation each promise to transfer to the customer either: (a) a good or service (or a bundle of goods or services) that is distinct; or (b) a series of distinct goods or services that are substantially the same and that have the same pattern of transfer to the customer."
    },
    {
        "rule_id": "INDAS115-05",
        "description": "Recognize revenue when (or as) the entity satisfies a performance obligation by transferring control of the asset to the customer.",
        "mapped_paragraphs": "31",
        "type": "Structural",
        "full_text": "An entity shall recognise revenue when (or as) the entity satisfies a performance obligation by transferring a promised good or service (ie. an asset) to a customer. An asset is transferred when (or as) the customer obtains control of that asset."
    },
    {
        "rule_id": "INDAS115-06",
        "description": "Recognize revenue over time if: customer consumes benefits simultaneously, controls asset as created, or asset has no alternative use and entity has right to payment.",
        "mapped_paragraphs": "35",
        "type": "Structural",
        "full_text": "An entity transfers control of a good or service over time and, therefore, satisfies a performance obligation and recognises revenue over time, if one of the following criteria is met: (a) the customer simultaneously receives and consumes the benefits provided by the entity’s performance as the entity performs...; (b) the entity’s performance creates or enhances an asset... that the customer controls as the asset is created or enhanced...; or (c) the entity’s performance does not create an asset with an alternative use to the entity... and the entity has an enforceable right to payment for performance completed to date."
    },
    {
        "rule_id": "INDAS115-07",
        "description": "Determine the transaction price including fixed consideration, variable consideration, financing components, non-cash consideration, and amounts payable to customers.",
        "mapped_paragraphs": "47–48",
        "type": "Numerical",
        "full_text": "An entity shall consider the terms of the contract and its customary business practices to determine the transaction price... When determining the transaction price, an entity shall consider the effects of all of the following: (a) variable consideration...; (b) constraining estimates of variable consideration...; (c) the existence of a significant financing component...; (d) non-cash consideration...; and (e) consideration payable to a customer..."
    },
    {
        "rule_id": "INDAS115-08",
        "description": "Treat penalties inherent in the determination of transaction price as variable consideration; otherwise, treat per the substance of the contract.",
        "mapped_paragraphs": "51AA",
        "type": "Numerical",
        "full_text": "In some contracts, penalties are specified. In such cases, penalties shall be accounted for as per the substance of the contract. Where the penalty is inherent in determination of transaction price, it shall form part of variable consideration... In other cases, the transaction price shall be considered as fixed."
    },
    {
        "rule_id": "INDAS115-09",
        "description": "Estimate variable consideration using 'expected value' or 'most likely amount' and constrain estimates to prevent significant revenue reversal.",
        "mapped_paragraphs": "53, 56",
        "type": "Numerical",
        "full_text": "An entity shall estimate an amount of variable consideration by using either... (a) The expected value... (b) The most likely amount... An entity shall include in the transaction price some or all of an amount of variable consideration estimated... only to the extent that it is highly probable that a significant reversal in the amount of cumulative revenue recognised will not occur when the uncertainty associated with the variable consideration is subsequently resolved."
    },
    {
        "rule_id": "INDAS115-10",
        "description": "Adjust transaction price for significant financing components unless the period between transfer and payment is one year or less (practical expedient).",
        "mapped_paragraphs": "60–63",
        "type": "Numerical",
        "full_text": "In determining the transaction price, an entity shall adjust the promised amount of consideration for the effects of the time value of money if... the contract contains a significant financing component... As a practical expedient, an entity need not adjust... if the entity expects, at contract inception, that the period between when the entity transfers a promised good or service... and when the customer pays... will be one year or less."
    },
    {
        "rule_id": "INDAS115-11",
        "description": "Allocate the transaction price to each performance obligation based on relative stand-alone selling prices.",
        "mapped_paragraphs": "74",
        "type": "Numerical",
        "full_text": "To meet the allocation objective, an entity shall allocate the transaction price to each performance obligation identified in the contract on a relative stand-alone selling price basis in accordance with paragraphs 76–80..."
    },
    {
        "rule_id": "INDAS115-12",
        "description": "Recognize incremental costs of obtaining a contract as an asset if recoverable; expense if amortization period is one year or less.",
        "mapped_paragraphs": "91, 94",
        "type": "Structural",
        "full_text": "An entity shall recognise as an asset the incremental costs of obtaining a contract with a customer if the entity expects to recover those costs... As a practical expedient, an entity may recognise the incremental costs of obtaining a contract as an expense when incurred if the amortisation period of the asset that the entity otherwise would have recognised is one year or less."
    },
    {
        "rule_id": "INDAS115-13",
        "description": "Recognize costs to fulfill a contract as an asset only if they relate directly to the contract, generate/enhance resources, and are recoverable.",
        "mapped_paragraphs": "95",
        "type": "Structural",
        "full_text": "If the costs incurred in fulfilling a contract with a customer are not within the scope of another Standard... an entity shall recognise an asset from the costs incurred to fulfil a contract only if those costs meet all of the following criteria: (a) the costs relate directly to a contract...; (b) the costs generate or enhance resources of the entity that will be used in satisfying... performance obligations in the future; and (c) the costs are expected to be recovered."
    },
    {
        "rule_id": "INDAS115-14",
        "description": "Present unconditional rights to consideration as 'Receivables' and conditional rights as 'Contract Assets'.",
        "mapped_paragraphs": "105–108",
        "type": "Structural",
        "full_text": "When either party to a contract has performed, an entity shall present the contract in the balance sheet as a contract asset or a contract liability... An entity shall present any unconditional rights to consideration separately as a receivable... A contract liability is an entity’s obligation to transfer goods or services to a customer for which the entity has received consideration... A contract asset is an entity’s right to consideration in exchange for goods or services that the entity has transferred to a customer."
    },
    {
        "rule_id": "INDAS115-15",
        "description": "Present separately the amount of excise duty included in the revenue recognized in the statement of profit and loss.",
        "mapped_paragraphs": "109AA",
        "type": "Disclosure",
        "full_text": "An entity shall present separately the amount of excise duty included in the revenue recognised in the statement of profit and loss."
    },
    {
        "rule_id": "INDAS115-16",
        "description": "Disaggregate revenue into categories that depict how economic factors affect the nature, amount, timing, and uncertainty of revenue.",
        "mapped_paragraphs": "114",
        "type": "Disclosure",
        "full_text": "An entity shall disaggregate revenue recognised from contracts with customers into categories that depict how the nature, amount, timing and uncertainty of revenue and cash flows are affected by economic factors."
    },
    {
        "rule_id": "INDAS115-17",
        "description": "Disclose opening and closing balances of receivables, contract assets, and contract liabilities.",
        "mapped_paragraphs": "116",
        "type": "Disclosure",
        "full_text": "An entity shall disclose all of the following: (a) the opening and closing balances of receivables, contract assets and contract liabilities from contracts with customers...; (b) revenue recognised in the reporting period that was included in the contract liability balance at the beginning of the period; and (c) revenue recognised in the reporting period from performance obligations satisfied (or partially satisfied) in previous periods..."
    },
    {
        "rule_id": "INDAS115-18",
        "description": "Disclose the aggregate transaction price allocated to remaining (unsatisfied) performance obligations and when revenue is expected to be recognized.",
        "mapped_paragraphs": "120",
        "type": "Disclosure",
        "full_text": "An entity shall disclose the following information about its remaining performance obligations: (a) the aggregate amount of the transaction price allocated to the performance obligations that are unsatisfied (or partially unsatisfied) as of the end of the reporting period; and (b) an explanation of when the entity expects to recognise as revenue the amount disclosed..."
    },
    {
        "rule_id": "INDAS115-19",
        "description": "Disclose significant judgements made regarding timing of satisfaction (over time vs. point in time) and determination of transaction price.",
        "mapped_paragraphs": "123",
        "type": "Disclosure",
        "full_text": "An entity shall disclose the judgements, and changes in the judgements, made in applying this Standard that significantly affect the determination of the amount and timing of revenue from contracts with customers. In particular... (a) the timing of satisfaction of performance obligations...; and (b) the transaction price and the amounts allocated to performance obligations..."
    },
    {
        "rule_id": "INDAS115-20",
        "description": "Reconcile revenue recognized in profit and loss with the contracted price, showing separately adjustments for discounts, rebates, refunds, etc.",
        "mapped_paragraphs": "126AA",
        "type": "Disclosure",
        "full_text": "An entity shall reconcile the amount of revenue recognised in the statement of profit and loss with the contracted price showing separately each of the adjustments made to the contract price, for example, on account of discounts, rebates, refunds, credits, price concessions, incentives, performance bonuses, etc., specifying the nature and amount of each such adjustment separately."
    },
    {
        "rule_id": "INDAS115-21",
        "description": "For Service Concession Arrangements: The operator shall not recognize infrastructure as Property, Plant and Equipment.",
        "mapped_paragraphs": "App C, 11",
        "type": "Structural",
        "full_text": "Infrastructure within the scope of this Appendix shall not be recognised as property, plant and equipment of the operator because the contractual service arrangement does not convey the right to control the use of the public service infrastructure to the operator."
    },
    {
        "rule_id": "INDAS115-22",
        "description": "For Service Concession Arrangements: Recognize consideration as a Financial Asset (unconditional right to cash) or Intangible Asset (right to charge users).",
        "mapped_paragraphs": "App C, 16–17",
        "type": "Structural",
        "full_text": "The operator shall recognise a financial asset to the extent that it has an unconditional contractual right to receive cash or another financial asset from or at the direction of the grantor for the construction services... The operator shall recognise an intangible asset to the extent that it receives a right (a licence) to charge users of the public service."
    }
  ]
}
}