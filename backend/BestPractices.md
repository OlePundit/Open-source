## GIT naming conventions and best practices
### Branch Naming

Branches created should be named using the following format:

```
{story type}-{2-3 word summary}
```

`story-type` - Indicates the context of the branch and should be one of:

- ft == Feature
- bg == Bug
- ch == Chore
- rf == Refactor

`story-summary` - Short 2-3 words summary about what the branch contains

**Example**

```
ft-resources-rest-endpoints
```

### PR Naming

The PR title should be named using the following format:

```
Story description
```

**Example**

```
Build out REST Endpoints for Resources (CRUD)
```

### PR Description Template (Markdown)

The description of the PR should contain the following headings and corresponding content in Markdown format.

```md
#### What does this PR do?
#### Description of Task to be completed?
#### How should this be manually tested?
#### Any background context you want to provide?
#### What are the relevant asana stories?
#### Screenshots (if appropriate)
#### Questions:
```

### Commits

Atomic commits should be made with the format:

```
<type>(<scope>): <subject>``<BLANK LINE> <body> <BLANK LINE> <footer>

```

Any line cannot be longer than 100 characters, meaning be concise.

```<type>``` should be:

 * feature
 * bug
 * chore
 * release
 * refactor
 * documentation
 * style
 * test

```<scope>``` should be something specific to the commit change. For example:

costume
 * django-setup
 * fighting-style
 * fan-base
 * logo and so on.

```<subject>``` text should:

 * use present tense: "save" not "saved" or "saving"
 * not capitalize first letter i.e no "Carry to safety"
 * not end with a dot (.)

**Message body (optional)** If a body is to be written, it should:

 * written in present tense.
 * include the reason for change and difference in the previous behaviour
