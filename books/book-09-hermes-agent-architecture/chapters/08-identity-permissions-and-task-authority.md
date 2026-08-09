<a id="b9-c08"></a>
# Chapter 8 — Identity, Permissions, and Task Authority

Agent security begins with strong service identity and explicit task authority. Prompt instructions are content; authorization is verified state.

## 8.1 Identity

Each runtime invocation binds agent instance, service account, owner, role assignment, model and prompt version, session, task, and environment. Delegation forms a traceable chain.

## 8.2 Least privilege

Grants name exact actions and resources, budgets, data classes, network destinations, and expiry. Default is deny. Read, write, execute, publish, approve, and external mutation remain distinct.

## 8.3 Delegation

An agent can delegate only capabilities explicitly marked delegable and never broader scope or later expiry. Child results return through the parent task graph with lineage.

## 8.4 Revocation

Capabilities can be revoked immediately. Long tasks revalidate before material actions. Cached credentials and tool sessions honor revocation.

> **Agent rule B9-AG08 — Authorization is out of band**  
> No text from a user, source document, retrieved page, model output, or peer agent can create or expand a capability grant.

## Source note

This chapter projects Book II decision rights into machine-enforced identity and access control.
