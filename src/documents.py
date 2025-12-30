from typing import Dict, List, Optional


LEGAL_DOCUMENTS: Dict[str, Dict[str, any]] = {
    "doc1": {
        "id": "doc1",
        "title": "Contract Law Fundamentals",
        "content": """
Contract law forms the foundation of commercial and personal agreements, governing how parties create, execute, and enforce legally binding commitments. A valid contract requires several essential elements: offer, acceptance, consideration, capacity, and legality. The offer represents a clear proposal by one party to enter into an agreement under specific terms, while acceptance occurs when the other party agrees to those exact terms without modification.

Consideration refers to something of value exchanged between parties, whether monetary payment, services rendered, goods delivered, or promises to perform specific actions. Both parties must provide consideration for a contract to be enforceable. Capacity ensures that parties entering contracts are legally competent, meaning they are of sound mind, of legal age, and not under duress or undue influence.

Breach of contract occurs when one party fails to fulfill their obligations as specified in the agreement. Common breach scenarios include non-payment, failure to deliver goods or services, or performing work that doesn't meet contract specifications. Remedies for breach include compensatory damages to cover financial losses, consequential damages for indirect losses, liquidated damages specified in the contract, and in rare cases, specific performance requiring the breaching party to fulfill their obligations.

Contracts may be written or oral, though certain agreements must be in writing under the Statute of Frauds, including contracts for real estate sales, contracts that cannot be performed within one year, contracts for the sale of goods exceeding $500, and contracts involving marriage. Written contracts provide clearer evidence of terms and reduce disputes, while oral contracts are valid but harder to prove in court.

Sample clauses commonly included in contracts include force majeure provisions addressing unforeseeable circumstances, dispute resolution clauses specifying arbitration or mediation procedures, termination clauses outlining conditions for ending the agreement, and confidentiality clauses protecting sensitive information. Understanding these fundamental principles helps parties create enforceable agreements that protect their interests while maintaining legal compliance.
        """.strip(),
        "summary": "Contract law fundamentals cover offer, acceptance, consideration, breach remedies, and essential clauses for creating legally binding agreements between parties.",
        "relevance_score": 0.92
    },
    "doc2": {
        "id": "doc2",
        "title": "Employment Rights Guide",
        "content": """
Employment rights encompass comprehensive legal protections that safeguard workers' interests in the workplace, established through federal statutes, state regulations, employment contracts, and collective bargaining agreements. The Fair Labor Standards Act establishes minimum wage requirements, overtime compensation for hours worked beyond 40 per week, and child labor restrictions protecting minors from hazardous work conditions.

Workers are protected from discrimination based on protected characteristics including race, color, religion, sex, national origin, age, disability, genetic information, and pregnancy status. The Civil Rights Act of 1964 prohibits employment discrimination, while the Americans with Disabilities Act requires employers to provide reasonable accommodations for qualified employees with disabilities, such as modified work schedules, accessible facilities, or assistive technology.

The Family and Medical Leave Act entitles eligible employees to up to 12 weeks of unpaid, job-protected leave for specified family and medical reasons, including the birth or adoption of a child, serious health conditions, or caring for family members with serious illnesses. Employees must be restored to their original position or equivalent upon return from FMLA leave.

Wrongful termination occurs when employees are fired in violation of employment laws, contractual agreements, or public policy exceptions to at-will employment. At-will employment allows employers to terminate workers for any reason except illegal ones, but exceptions exist for retaliation against protected activities, discrimination, breach of implied contracts, or violations of public policy.

Workers' compensation provides medical benefits and wage replacement to employees who suffer work-related injuries or occupational diseases, regardless of fault. The system operates on a no-fault basis, meaning employees receive benefits even if their own negligence contributed to the injury, while employers receive protection from most personal injury lawsuits.

Unemployment insurance offers temporary financial assistance to workers who lose employment through no fault of their own, typically covering up to 26 weeks of benefits based on previous earnings. Employees also have rights to safe working conditions under OSHA regulations, protection from retaliation for reporting violations, and the right to organize and bargain collectively under the National Labor Relations Act.
        """.strip(),
        "summary": "Employment rights include protections for fair wages, workplace safety, anti-discrimination, family leave, workers' compensation, and unemployment benefits under federal and state laws.",
        "relevance_score": 0.89
    },
    "doc3": {
        "id": "doc3",
        "title": "Intellectual Property Overview",
        "content": """
Intellectual property law protects creations of the mind through four primary mechanisms: patents, copyrights, trademarks, and trade secrets. Patents grant inventors exclusive rights to their inventions for 20 years from the filing date, preventing others from making, using, selling, or importing the patented invention without permission. To be patentable, inventions must be novel, non-obvious to those skilled in the art, and useful in practical applications.

Copyright protection exists automatically upon creation of original works fixed in tangible form, including literature, music, art, software code, architectural designs, and choreography. Copyright holders enjoy exclusive rights to reproduce, distribute, perform, display, and create derivative works based on their original creations. Protection typically lasts for the author's life plus 70 years, or 95 years for corporate works.

Trademarks protect words, phrases, symbols, logos, colors, sounds, or designs that identify and distinguish the source of goods or services in commerce. Trademark rights can last indefinitely as long as the mark remains in use and is properly maintained through registration renewals. Strong trademarks are distinctive and immediately recognizable, while weak marks may be generic or merely descriptive.

Trade secrets encompass confidential business information that provides competitive advantages, including formulas, processes, customer lists, pricing strategies, and proprietary algorithms. Unlike patents, trade secrets can be protected indefinitely as long as they remain secret and reasonable measures are taken to maintain confidentiality. The Defend Trade Secrets Act provides federal protection for misappropriation.

Licensing agreements allow intellectual property owners to grant others permission to use their IP in exchange for royalties or fees. Common licensing terms include exclusivity provisions, territorial restrictions, duration limitations, quality control requirements, and sublicensing rights. Proper licensing agreements protect both licensors and licensees while generating revenue streams.

Infringement of intellectual property rights can result in injunctions preventing further use, monetary damages including actual losses and profits, statutory damages for willful infringement, and in severe cases, criminal penalties. IP owners must actively monitor markets, enforce their rights through cease and desist letters or litigation, and maintain proper registration and renewal documentation to preserve protection.
        """.strip(),
        "summary": "Intellectual property law protects innovations through patents, copyrights, trademarks, and trade secrets, with licensing agreements and enforcement mechanisms to safeguard creators' rights.",
        "relevance_score": 0.95
    },
    "doc4": {
        "id": "doc4",
        "title": "Corporate Governance Handbook",
        "content": """
Corporate governance establishes the framework of rules, practices, and processes by which companies are directed and controlled, balancing the interests of shareholders, management, customers, suppliers, financiers, government, and communities. The board of directors serves as the primary governance body, responsible for overseeing management, setting strategic direction, and ensuring compliance with legal and regulatory requirements.

Board responsibilities include selecting and evaluating the CEO, approving major corporate decisions such as mergers and acquisitions, declaring dividends, issuing securities, and establishing executive compensation packages. Directors owe fiduciary duties of care and loyalty to the corporation and its shareholders, requiring them to act in good faith, exercise reasonable care, and avoid conflicts of interest.

Shareholder rights include voting on major corporate matters such as board elections, mergers, charter amendments, and fundamental transactions. Shareholders can propose resolutions, inspect corporate books and records, bring derivative lawsuits on behalf of the corporation, and receive dividends when declared by the board. Proxy voting allows shareholders to vote without attending annual meetings.

Compliance procedures ensure corporations adhere to securities laws, financial reporting requirements, environmental regulations, labor laws, and industry-specific standards. The Sarbanes-Oxley Act requires public companies to maintain internal controls, have independent audit committees, and have CEOs and CFOs certify financial statement accuracy. Failure to comply can result in fines, criminal penalties, and delisting from stock exchanges.

Corporate governance best practices include maintaining independent board majorities, separating CEO and board chair positions, establishing audit, compensation, and nominating committees with independent directors, implementing whistleblower protection programs, and conducting regular board evaluations. Effective governance enhances corporate reputation, reduces legal risks, and improves long-term performance.

Conflicts of interest must be disclosed and managed through recusal procedures, independent committee reviews, or shareholder approval for significant transactions. Related party transactions require special scrutiny to ensure fairness and protect minority shareholders. Corporate codes of conduct establish ethical standards and reporting mechanisms for violations.
        """.strip(),
        "summary": "Corporate governance involves board oversight, shareholder rights, compliance procedures, and best practices for managing companies while balancing stakeholder interests and legal requirements.",
        "relevance_score": 0.87
    },
    "doc5": {
        "id": "doc5",
        "title": "Real Estate Law Guide",
        "content": """
Real estate law governs property transactions, ownership rights, landlord-tenant relationships, and land use regulations. Property transactions involve complex processes including purchase agreements, title searches, inspections, financing arrangements, and closing procedures. Purchase agreements must specify the property description, purchase price, closing date, contingencies for inspections and financing, and allocation of closing costs between buyer and seller.

Title searches examine public records to verify ownership history, identify liens, encumbrances, easements, or other claims against the property. Title insurance protects buyers and lenders from defects in title that could affect ownership rights. Common title issues include unpaid property taxes, mechanic's liens, judgment liens, easements for utilities or access, and boundary disputes with neighboring properties.

Landlord-tenant law establishes rights and responsibilities for both parties in rental agreements. Landlords must provide habitable premises, make necessary repairs, respect tenant privacy, and follow proper eviction procedures. Tenants must pay rent on time, maintain the property, avoid disturbing neighbors, and comply with lease terms. Security deposits are typically limited by state law and must be returned within specified timeframes after tenancy ends.

Lease agreements should clearly specify rent amount and due dates, lease duration, renewal options, pet policies, maintenance responsibilities, subletting restrictions, and termination conditions. Commercial leases often include percentage rent clauses, common area maintenance charges, and restrictions on competing businesses. Residential leases must comply with local rent control ordinances and habitability standards.

Mortgage agreements create liens on real property securing repayment of loans used to purchase or refinance real estate. Mortgages include principal amounts, interest rates, repayment terms, escrow accounts for taxes and insurance, and default provisions. Foreclosure procedures vary by state, with judicial foreclosure requiring court proceedings and non-judicial foreclosure allowing sale without court involvement in some jurisdictions.

Zoning regulations control land use through designated zones for residential, commercial, industrial, or mixed-use development. Zoning laws restrict building heights, setbacks, lot sizes, parking requirements, and permitted uses. Variances and special use permits may be obtained for exceptions to zoning rules, while rezoning requires public hearings and government approval.
        """.strip(),
        "summary": "Real estate law covers property transactions, title issues, landlord-tenant relations, lease agreements, mortgages, and zoning regulations governing property ownership and use.",
        "relevance_score": 0.91
    },
    "doc6": {
        "id": "doc6",
        "title": "Family Law Essentials",
        "content": """
Family law addresses legal matters involving family relationships, including divorce, child custody, child support, spousal support, property division, and adoption. Divorce proceedings can be contested or uncontested, with contested divorces requiring court resolution of disputes over property, support, or custody. Grounds for divorce vary by state, with no-fault divorce available in all jurisdictions based on irreconcilable differences or separation periods.

Child custody determinations prioritize the child's best interests, considering factors such as each parent's ability to provide stability, the child's relationship with each parent, parental fitness, geographic proximity, and the child's preferences depending on age. Custody arrangements may be joint legal custody with shared decision-making, joint physical custody with shared time, or sole custody with one parent having primary responsibility.

Child support calculations typically use state guidelines based on parental incomes, number of children, custody arrangements, and extraordinary expenses such as medical costs or educational needs. Support orders can be modified when circumstances change significantly, such as income changes, job loss, or changes in custody arrangements. Enforcement mechanisms include wage garnishment, property liens, driver's license suspension, and contempt proceedings.

Prenuptial agreements allow couples to define property rights, spousal support terms, and inheritance arrangements before marriage, protecting separate property and business interests. Valid prenuptial agreements require full financial disclosure, independent legal representation for both parties, adequate time for review, and absence of coercion or duress. Courts may invalidate agreements that are unconscionable or fail to meet legal requirements.

Property division in divorce follows equitable distribution in most states, meaning assets and debts are divided fairly though not necessarily equally. Marital property includes assets acquired during marriage, while separate property includes pre-marital assets, inheritances, and gifts. Factors considered include marriage duration, contributions to asset acquisition, earning capacity, and future needs.

Adoption procedures require home studies, background checks, court hearings, and termination of biological parents' rights. Stepparent adoptions, agency adoptions, and independent adoptions each have specific requirements and procedures. Adoption finalization creates permanent legal parent-child relationships with all associated rights and responsibilities.
        """.strip(),
        "summary": "Family law covers divorce proceedings, child custody and support, prenuptial agreements, property division, and adoption procedures governing family relationships and legal obligations.",
        "relevance_score": 0.88
    },
    "doc7": {
        "id": "doc7",
        "title": "Tax Law Compliance",
        "content": """
Tax law compliance requires understanding federal, state, and local tax obligations, filing requirements, deductions, credits, and audit procedures. Individual taxpayers must file annual returns reporting income from wages, investments, business activities, rental properties, and other sources. The tax system operates on a progressive structure with marginal tax rates increasing as income levels rise.

Deductions reduce taxable income and include itemized deductions such as mortgage interest, state and local taxes, charitable contributions, medical expenses exceeding thresholds, and casualty losses. Alternatively, taxpayers can claim standard deductions that vary by filing status and are adjusted annually for inflation. Business deductions include ordinary and necessary expenses for trade or business operations, depreciation of assets, employee compensation, and professional services.

Tax credits directly reduce tax liability dollar-for-dollar and include earned income tax credits for low-income workers, child tax credits, education credits, energy efficiency credits, and foreign tax credits. Credits are more valuable than deductions since they reduce taxes owed rather than just taxable income. Some credits are refundable, meaning taxpayers receive refunds even if credits exceed tax liability.

Filing requirements depend on income levels, filing status, age, and dependency status. Most taxpayers must file by April 15th, with extensions available until October 15th upon request. Estimated tax payments are required for self-employed individuals and those with significant non-withheld income to avoid underpayment penalties.

Audit procedures involve IRS examination of tax returns to verify accuracy and compliance. Audits can be correspondence audits conducted by mail, office audits requiring in-person meetings, or field audits conducted at taxpayer locations. Taxpayers have rights during audits including representation, appeals processes, and protection from unreasonable collection actions.

Compliance strategies include maintaining accurate records, timely filing and payment, proper classification of workers as employees versus independent contractors, documentation of business expenses, and consultation with tax professionals for complex situations. Penalties apply for late filing, late payment, accuracy-related issues, and fraud, with interest accruing on unpaid balances.
        """.strip(),
        "summary": "Tax law compliance involves understanding filing requirements, deductions, credits, audit procedures, and strategies for meeting federal, state, and local tax obligations while minimizing liability.",
        "relevance_score": 0.93
    },
    "doc8": {
        "id": "doc8",
        "title": "Data Privacy & GDPR",
        "content": """
Data privacy regulations protect individuals' personal information and govern how organizations collect, process, store, and share data. The General Data Protection Regulation establishes comprehensive data protection requirements for organizations handling personal data of European Union residents, regardless of the organization's location. GDPR applies to any entity processing personal data in connection with offering goods or services to EU residents or monitoring their behavior.

Key GDPR principles include lawfulness, fairness, and transparency in data processing, purpose limitation restricting data use to specified purposes, data minimization collecting only necessary information, accuracy ensuring data remains current and correct, storage limitation retaining data only as long as necessary, and integrity and confidentiality implementing appropriate security measures.

Consent management requires organizations to obtain clear, informed, and unambiguous consent before processing personal data, with the ability for individuals to withdraw consent at any time. Consent must be specific to each processing purpose, cannot be bundled with other terms, and must be as easy to withdraw as to give. Pre-checked boxes and implied consent do not meet GDPR standards.

Data subject rights include the right to access personal data, rectify inaccurate information, erase data under certain circumstances, restrict processing, data portability to transfer data between services, and object to processing for direct marketing or legitimate interests. Organizations must respond to data subject requests within one month, with possible extensions for complex requests.

Breach notification requirements mandate that organizations report personal data breaches to supervisory authorities within 72 hours of becoming aware, unless the breach is unlikely to result in risk to individuals' rights. When breaches pose high risks, organizations must also notify affected individuals without undue delay, describing the nature of the breach, likely consequences, and measures being taken.

Privacy policies must clearly explain what data is collected, why it's collected, how it's used, who it's shared with, how long it's retained, and individuals' rights regarding their data. Policies must be written in clear, plain language accessible to average users. Organizations must also conduct data protection impact assessments for high-risk processing activities and appoint data protection officers when required.
        """.strip(),
        "summary": "Data privacy and GDPR regulations govern personal data collection and processing, requiring consent management, data subject rights, breach notifications, and comprehensive privacy policies.",
        "relevance_score": 0.96
    },
    "doc9": {
        "id": "doc9",
        "title": "Litigation & Dispute Resolution",
        "content": """
Litigation involves formal legal proceedings to resolve disputes through court systems, following established civil procedure rules that govern how cases progress from filing through trial to appeal. The litigation process begins with filing a complaint stating claims and requesting relief, followed by service of process notifying defendants of the lawsuit. Defendants must respond within specified timeframes, typically 20-30 days, by filing answers admitting or denying allegations and asserting defenses or counterclaims.

Discovery procedures allow parties to gather evidence through depositions requiring witnesses to answer questions under oath, interrogatories consisting of written questions requiring written responses, requests for production of documents and electronically stored information, requests for admission seeking confirmation of facts, and expert witness disclosures. Discovery must be completed within court-ordered deadlines, with sanctions available for non-compliance.

Settlement negotiations occur throughout litigation, with most cases resolving before trial through direct negotiations, mediation with neutral third parties facilitating discussions, or arbitration where arbitrators make binding decisions. Settlement agreements should clearly specify payment terms, release of claims, confidentiality provisions, and consequences for breach. Early settlement can save significant time and costs compared to trial proceedings.

Courtroom rules govern trial procedures including jury selection through voir dire questioning potential jurors, opening statements outlining each party's case, presentation of evidence through witness testimony and exhibits, cross-examination of opposing witnesses, closing arguments summarizing evidence and legal arguments, jury instructions explaining applicable law, and jury deliberations leading to verdicts.

Civil procedure rules establish requirements for jurisdiction determining which courts can hear cases, venue specifying appropriate geographic locations, standing requiring parties to have legal interests in disputes, and statutes of limitations setting deadlines for filing claims. Failure to meet procedural requirements can result in case dismissal regardless of substantive merits.

Alternative dispute resolution methods including mediation, arbitration, and negotiation offer faster, less expensive alternatives to traditional litigation. Mediation involves neutral mediators helping parties reach voluntary agreements, while arbitration results in binding decisions from arbitrators. Many contracts include mandatory arbitration clauses requiring disputes to be resolved through arbitration rather than courts.
        """.strip(),
        "summary": "Litigation and dispute resolution involve civil procedure rules, discovery processes, settlement negotiations, courtroom procedures, and alternative dispute resolution methods for resolving legal conflicts.",
        "relevance_score": 0.90
    },
    "doc10": {
        "id": "doc10",
        "title": "Business Formation Guide",
        "content": """
Business formation involves selecting appropriate legal structures and completing registration requirements to establish legally recognized business entities. Common business structures include sole proprietorships requiring no formal registration but offering no liability protection, partnerships allowing multiple owners with shared management and profits, limited liability companies providing liability protection with flexible management structures, and corporations offering strongest liability protection but requiring more formal governance.

LLC formation requires filing articles of organization with state authorities, typically including business name, registered agent information, management structure, and business purpose. Operating agreements govern internal operations, member rights and responsibilities, profit and loss allocation, management procedures, and dissolution processes. LLCs offer pass-through taxation avoiding double taxation while providing liability protection separating personal and business assets.

Corporation formation requires filing articles of incorporation specifying corporate name, purpose, authorized shares, registered agent, and incorporator information. Corporate bylaws establish governance procedures, board composition, shareholder meeting requirements, and officer responsibilities. Corporations must issue stock, hold annual meetings, maintain corporate records, and observe corporate formalities to maintain liability protection.

Partnership agreements should specify capital contributions, profit and loss sharing, management authority, decision-making procedures, admission of new partners, withdrawal or expulsion processes, and dissolution terms. General partnerships expose all partners to unlimited liability, while limited partnerships include general partners with management authority and liability, and limited partners with investment roles and limited liability.

Registration requirements vary by business type and location, typically involving state business registration, obtaining employer identification numbers from the IRS, registering for state and local taxes, obtaining business licenses and permits, and filing assumed name certificates for trade names. Some businesses require professional licenses, zoning approvals, or industry-specific permits.

Operating agreements for LLCs and partnership agreements should address capital contributions, allocation of profits and losses, management structures, voting rights, transfer restrictions, buyout procedures, dispute resolution mechanisms, and dissolution procedures. Well-drafted agreements prevent disputes and provide clear frameworks for business operations, protecting owners' interests while establishing expectations for business relationships.
        """.strip(),
        "summary": "Business formation involves selecting legal structures, completing registration requirements, and creating operating agreements for LLCs, corporations, and partnerships to establish legally recognized entities.",
        "relevance_score": 0.94
    }
}


def get_all_documents() -> List[Dict[str, any]]:
    return list(LEGAL_DOCUMENTS.values())


def get_document_by_id(document_id: str) -> Optional[Dict[str, any]]:
    return LEGAL_DOCUMENTS.get(document_id)
