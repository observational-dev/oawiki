# Example Page

Rather than being intended for wiki viewers, this page exists for wiki editors. You could be one!

## Markdown Examples

If you've used Discord or Reddit, these might be familiar to you.

**Text that is bolded**

_Italicized text_

~~struckthrough text~~

fun `inline code` format[^myref]
% this line is a comment, and won't be displayed on the wiki. I just wanted to point out that the footnote definitions will always be displayed at the end of the page, but it's useful to define them near where they are used.
[^myref]: This is an auto-numbered footnote definition

A quick markdown [cheatsheet](https://commonmark.org/help/) is available, as well as a [comprehensive catalog](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html#syntax-core) for MyST's implementation which is used here.

...And a cat image for you:[^catref]
[^catref]: Locke, 2023, used with permission

![a cat yawns, Locke 2023, used with permission](https://cdn.discordapp.com/attachments/514888013533151253/1157127122570190998/PXL_20230929_012816945.PORTRAIT.jpg)

> This is a blockquote. It's useful for separating out a specific chunk of text from the rest. Glass does not flow at room temperature as a high-viscosity liquid. Although glass shares some molecular properties with liquids, it is a solid at room temperature and only begins to flow at hundreds of degrees above room temperature. Old glass which is thicker at the bottom than at the top comes from the production process, not from slow flow; no such distortion is observed in other glass objects of similar or even greater age
> _Wikipedia [List of Common Misconceptions](https://en.m.wikipedia.org/wiki/List_of_common_misconceptions)_

### Other items

- List
- List
- List

Horizontal rule:

---

1. One
2. Two
3. Three

```
Code block
Probably less used on this wiki, but included here for reference
```

## Tricks Beyond Markdown

You can do some neat dropdown bits if you want:

```{dropdown} What does a dropdown look like?

Like this :)

```

```{dropdown} That's cool, can you do another, fancier one?
:icon: comment-discussion
:animate: fade-in-slide-down
Absolutely! It's documented [here](https://sphinx-design.readthedocs.io/en/latest/dropdowns.html), with the change that we use backticks instead of colon fences.
```

Additionally, sub- and superscripts are supported. H{sub}`2`O, and 4{sup}`th` of July

---

Thank you for taking the time to contribute to this repository of knowledge!

Happy editing!
