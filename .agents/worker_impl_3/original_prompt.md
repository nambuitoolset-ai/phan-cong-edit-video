## 2026-06-07T17:34:11Z
You are Worker 3.
Your working directory is /tmp/phan-cong-edit-video-deploy/.agents/worker_impl_3/.
Your task is to fix the styling and bugs in the 2 remaining pages: /phan-cong-edit-video/index.html and /bang-tinh-luong-thuong/index.html, according to the Lark Style Design System guidelines, while keeping all dynamic logic, scripts, and events fully intact.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Detailed Instructions:

1. Update /tmp/phan-cong-edit-video-deploy/bang-tinh-luong-thuong/index.html:
- Fix the mobile menu burger toggle (lines 525-542): change "mobileMenu.classList.add('active')" and "mobileMenu.classList.remove('active')" to "mobileMenu.classList.add('open')" and "mobileMenu.classList.remove('open')" respectively.
- Fix days off input validation (line 585): change the inline oninput handler to:
  oninput="this.value=this.value.replace(/[^0-9]/g,''); const D=daysOf(+document.getElementById('sel-m').value, +document.getElementById('inp-y').value); if(+this.value>D)this.value=D; calculate();"
- Implement "autoFillDays()" (line 571) as:
  function autoFillDays() {
    const m = +document.getElementById('sel-m').value;
    const y = +document.getElementById('inp-y').value;
    const D = daysOf(m, y);
    EMP.forEach(e => {
      const inp = document.getElementById('off-' + e.id);
      if (inp) {
        if (+inp.value > D) inp.value = D;
      }
    });
    calculate();
  }
- Change month and year inputs to trigger auto-recalculation when changed:
  - Month select (line 485): onchange="autoFillDays()" (since autoFillDays calls calculate, this is sufficient).
  - Year input (line 488): oninput="this.value=this.value.replace(/[^0-9]/g,''); autoFillDays();"
- Fix the non-secure context clipboard bug (line 573) in copyText:
  function copyText(text, btn) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        btn.textContent = 'Đã copy';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.textContent = 'Copy';
          btn.classList.remove('copied');
        }, 2000);
      });
    } else {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        document.execCommand('copy');
        btn.textContent = 'Đã copy';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.textContent = 'Copy';
          btn.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Fallback copy failed', err);
      }
      document.body.removeChild(textArea);
    }
  }
- In calculate() function (line 628-630), double-safeguard the days off subtraction to prevent negative values:
  const off = Math.min(D, +document.getElementById('off-' + e.id).value || 0);
  const worked = Math.max(0, D - off);

2. Update /tmp/phan-cong-edit-video-deploy/phan-cong-edit-video/index.html:
- Apply visual styling to match the Lark Style Design System.
- Add Google Fonts for Be Vietnam Pro and link to relative stylesheet "../style.css?v=9".
- Define CSS rule for body:
  body {
    font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    background: var(--bg-soft);
    color: var(--text);
    padding-top: 80px; /* offset for fixed navbar */
    padding-bottom: 80px; /* offset for fixed footer */
  }
- Change overall styles, title, cards, and buttons to use design variables (var(--card-bg), var(--border), var(--text), var(--blue), var(--blue-hover)).
- Offset body for the fixed navbar/footer (padding-top: 80px, padding-bottom: 80px).
- Add the navbar section at the top of the body (identical to quan-ly-team/index.html navbar).
- Add the mobile menu overlay (identical to quan-ly-team/index.html mobile menu overlay).
- Add a footer at the bottom of the body (identical to other pages, e.g. '© 2026 namoinam.com • Lark Style Design System').
- Add the mobile menu burger control script in the script block. Make sure to toggle class 'open' (not 'active').
- Absolutely preserve all existing dynamic script block contents (const EMPLOYEES = ..., let historyData = ..., dates = ..., idx = ..., function cardName, fmtDate, updateNav, render, navigate, init). Do not delete or corrupt any scripts, dynamic data tables, or fetch requests.

Note: Direct file edits might time out. We recommend writing or overwriting files using run_command with "cat << 'EOF' > [file_path]" shell redirection.

Once you have completed the implementations, perform verification checks to ensure pages render correctly and contain no JavaScript or HTML syntax errors. Write a handoff report at /tmp/phan-cong-edit-video-deploy/.agents/worker_impl_3/handoff.md and report back via message.
