
# Assignment 2 - Grammar Writing - Answers


<div class="page">

## Part 1


### Why does the program generate so many long sentences?

The main origin for long sentences is the rule:

    1	NP	NP PP

Because this is the only recursive rule.
This rule is taking 1/2 odds to be chosen each time we see the parameter `NP`
And we have the parameter `NP` at least 2 times:

* once derived from `S` parameter
* secondly from `VP`

So, in conclusion the odds to **not** choose the recursive rule at all is: `1/2 * 1/2 = 1/4`
And `1/2` to get at least one (which in his turn also can choose a recursive turn).


### Why do the generated sentences rarely have multiple adjectives?

Again, let's look about the responsible rule for multiple adjectives:

    1	Noun	Adj Noun

In addition to this rule we also have 5 more rules for `Noun`:

    1	Noun	president
    1	Noun	sandwich
    1	Noun	pickle
    1	Noun	chief of staff
    1	Noun	floor

As a result, the odds to get multiple adjectives is `1/6`

</div><div class="page">

## Part 2

### Modifications to the grammar:

 1. Added more words to the second section of the grammar:

    1. Nouns
    2. Names
    3. Verbs (past)
    4. Verbs (present progressive)

 2. Distinguish plural vs singular (on present progressive) - more about that
    is elaborated on the "problems" section.

 3. Distinguish different types of verbs:

    1. Verbs that need a Noun after them (`VPN`)
    2. Verbs that come alone (`VPU`)
    3. Verbs from each type of the above that can come also with a "that" (like `"he thought that..."`) (`VPNT` / `VPUT`)
    4. Verbs that come alone but can have a referring noun like `"thinking of / working on something"` (`VPO`)

 4. Add an option for connecting things with "and".
    We added special variables for that, so they create only verbs/nouns that supports that kind of stuff.

### Problems and how we overcome them:

 1. First: **The problems with (b) and (h)/(i)** as we understood are:

      - Plural vs singular on present progressive. Which means - if we want
          to allow sentences like `"Sally and the president ate .."` it can also derive
          sentences like: `"Sally and the presidant is eating .."` which is
          grammaticly wrong. <br/>
          We solved this one (next bullet).
  
      - Mixes of tenses like: `"wokred and is kissing.."` which can also derive wierd sentences.

 2. **Plural vs Singular:**<br/>
    In order to solve this, we added a flag when we turn the subject
    of the sentence to Plural. So, in case we would like to use present progressive
    we would add "are" and not "is".

    *Note:* This caused derivatives which created wierd sentences if
    combined with the "and" feature on the verbs (bullet #4 of above).
    To avoid this, we decided to allow **only past simple verbs** iff the Grammar chose
    to use the "add" between verbs. (this can also be related to second problem mentioned above).

 3. **"kissed and ate and kissed and ate...":** <br/>
    To avoid this weird "endless and" we
    give an option in the middle of the rule to add the Noun so the sentence will be more
    like: `"kissed and ate *a sandwich* and kissed and ate..."`

</div><div class="page">

## Part 3

### Done



## Part 4

### Solution discussions

#### Chosen phenomena:

 * (c) **Relative clauses**

 * (e) **Singular vs. plural agreement**

#### Discussion:

 * for (c) we had to copy some of our rules and adjust them to fit with the phenomenon.
    In general, we added new NP rule to support nouns that have a "that..." description.
    This rule is the root for all section (c) derivatives.
    This approach gave us the ability to combine this phenomenon with all the
    sentences which we already derive.

    We noted that sample 3 of this phenomenon is a combination with
    new phenomenon and one of the first two phenomena so we used our rules for 1 and 2
    and combine them with new rule to fit the third phenomenon.

 * for (e) part we have done half of the work in part 2 as we mentioned on the `plural vs singular` section.
    In details, we had a rule which called **PNP** which refer to a "plural NP",
    this rule creates subjects like: `"Sally **and** the president.."` .<br />
    In the first stage we added also a plural nouns to this rule like "the citizens".<br/>
    The second stage was to add the present simple verbs and adjust them according the singular/plural tense.

    *Note:* We chose in part 2 to include **only past simple** when we
    have plural subject and more than one verb. Here we had to also include
    present simple verbs.


</div>
