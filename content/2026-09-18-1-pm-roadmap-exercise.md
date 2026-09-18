Title: Thinking Like a PM: A Roadmap Exercise on a Tool I Already Built
Date: 2026-09-18
Category: Product Thinking
Tags: Product Management, Roadmapping, Prioritization, Career Transition
Slug: pm-roadmap-exercise
Author: Priyanshu Bishnoi
Summary: A self-initiated practice exercise in product thinking — prioritizing the next two quarters for an internal tool I built, using the same rigor I'd bring to system design.

## Why I'm Writing This

Most of what's on this blog is systems thinking — request flows, DLL boundaries, CAP theorem. Lately I've been deliberately applying that same rigor one layer up: not just *how do I build this correctly*, but *what should get built next, and why*.

This post is a practice exercise, not a formal deliverable from work — I wasn't asked to write a roadmap for this tool. I picked something I already built and own end-to-end, and forced myself to prioritize it the way a PM would: real constraints, real trade-offs, no hand-waving.

## 🧩 1. The Problem, Restated Like an Engineer Would

A while back I built an internal expense-management tool to replace a fully manual, spreadsheet-based process. It's been running for a while now — adoption across 100+ employees, and it eliminates roughly 30 hours of manual work a month (it used to take two people's time to keep the old process running).

But shipping v1 isn't the end of the story. Looking at usage patterns and informal feedback since launch, three gaps stand out:

1. **No mobile-friendly submission flow** — desktop-only, which is a real friction point for a workforce that isn't always at a desk.
2. **Approval bottlenecks** — if a manager is on leave, the claim just sits. No delegate, no escalation.
3. **No pre-submission validation** — policy violations get caught *after* submission, causing rework and rejection cycles.

None of these are technically hard. The interesting part is deciding what to do first.

## 🧩 2. Who Actually Uses This

**Primary:** employees submitting claims.
**Secondary:** approving managers, and Finance reconciling monthly reports.

Worth stating explicitly, because the three gaps above don't affect these groups equally — the mobile gap hits primary users daily, the approval bottleneck hits secondary users intermittently but painfully, and the validation gap hits both, just at different points in the cycle.

## 🧩 3. Picking What Matters: A RICE-ish Framework

I didn't want to prioritize by gut feeling, so I forced myself through a lightweight reach/impact pass on each gap:

| Feature | Why Now | Impact |
|---|---|---|
| Mobile-responsive submission flow | Largest usage gap; blocks further adoption growth | High reach, high impact |
| Manager delegate / escalation for approvals | Removes a single point of failure in the approval cycle | Medium reach, high impact |
| Pre-submission policy validation | Cuts rework, reduces Finance back-and-forth | Medium reach, medium impact |

The mobile flow wins on reach alone — it affects every submission, every time. The approval fix has a smaller blast radius but a sharper pain point when it hits. Validation is real, but it's the one I'd cut first if timelines got tight.

## 🧩 4. The Two-Quarter Plan

**Q1:** Design, build, and ship the mobile-responsive submission flow.

**Q2:** Build manager delegate/escalation and policy validation in parallel, with a mid-quarter checkpoint for Finance to sign off on the validation rules before they go live.

The sequencing isn't arbitrary — mobile is standalone and low-dependency, so it can move fast. The Q2 items both touch approval workflow, so building them together (even if they ship on slightly different timelines) avoids re-touching the same code path twice.

## 🧩 5. What Could Go Wrong (Because Something Always Does)

* **Policy validation rules need Finance sign-off**, and Finance's calendar isn't mine to control. If that sign-off slips, validation slips — mobile and delegate/escalation don't get held hostage to it.
* **"Delegate" sounds simple until you ask "who chooses the delegate, and when?"** If it's chosen reactively (after someone's already on leave), it's not actually solving the bottleneck. Delegates need to be set up in advance, not scrambled together mid-crisis.
* **Success metrics need to exist before launch, not after.** Approval cycle time, % of mobile submissions, rejection rate — if I don't instrument these from day one, I won't actually know if any of this worked.

## ✅ Takeaway

Prioritization is just another system design problem. You've got constraints (Finance's calendar, engineering time), trade-offs (reach vs. impact vs. effort), and failure modes you need a plan for *before* they happen, not after. The same instinct that makes me ask "what happens when this service goes down" is the instinct that makes me ask "what happens when this feature ships and nobody adopts it." Different domain, same muscle.
