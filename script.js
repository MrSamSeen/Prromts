document.addEventListener('DOMContentLoaded', () => {
    const app = document.getElementById('app');
    const isArchive = document.body.classList.contains('page-archive');
    let allPrompts = [];

    // Config
    const ITEMS_PER_PAGE = 24;
    let currentPage = 1;

    // Fetch data
    fetch('prompts.json')
        .then(response => {
            if (!response.ok) throw new Error('Failed to load prompts');
            return response.json();
        })
        .then(data => {
            allPrompts = data;
            init();
        })
        .catch(err => {
            console.error(err);
            app.innerHTML = '<p style="text-align:center; color: #ff5555;">Error loading prompts. Please try again later.</p>';
        });

    function init() {
        if (isArchive) {
            handleArchiveView();
        } else {
            handleHomeView();
        }
    }

    function handleHomeView() {
        // Shuffle and pick 8
        const shuffled = [...allPrompts].sort(() => 0.5 - Math.random());
        const selected = shuffled.slice(0, 9);
        renderPrompts(selected);
    }

    function handleArchiveView() {
        const urlParams = new URLSearchParams(window.location.search);
        const category = urlParams.get('category');
        const tag = urlParams.get('tag');
        const pageParam = parseInt(urlParams.get('page')) || 1;
        currentPage = pageParam;

        let filtered = allPrompts;
        const titleEl = document.getElementById('archive-title');

        if (category) {
            filtered = allPrompts.filter(p => p.category === category);
            titleEl.textContent = `Category: ${category}`;
            document.title = `${category} - AI Prompts Archive`;
        } else if (tag) {
            filtered = allPrompts.filter(p => p.tags && p.tags.includes(tag));
            titleEl.textContent = `Tag: #${tag}`;
            document.title = `#${tag} - AI Prompts Archive`;
        }

        renderPagination(filtered);

        // Slice for current page
        const start = (currentPage - 1) * ITEMS_PER_PAGE;
        const end = start + ITEMS_PER_PAGE;
        const pageItems = filtered.slice(start, end);

        if (pageItems.length === 0) {
            app.innerHTML = '<div style="text-align:center; padding:2rem;">No prompts found. <a href="archive.html" style="color:var(--accent-color)">View all</a></div>';
        } else {
            renderPrompts(pageItems);
        }
    }

    function renderPrompts(prompts) {
        app.innerHTML = prompts.map(prompt => `
            <article class="prompt-card">
                <div class="card-header">
                    <a href="archive.html?category=${encodeURIComponent(prompt.category)}" class="card-category">
                        ${escapeHtml(prompt.category)}
                    </a>
                </div>
                <h2 class="card-title">${escapeHtml(prompt.title)}</h2>
                <div class="card-body">
                    <div class="prompt-text">${escapeHtml(prompt.prompt)}</div>
                </div>
                <div class="card-footer">
                    <div class="tags-container">
                        ${(prompt.tags || []).map(t => `<a href="archive.html?tag=${encodeURIComponent(t)}" class="tag-pill">#${escapeHtml(t)}</a>`).join('')}
                    </div>
                    <button class="copy-btn" onclick="copyToClipboard(this, '${escapeJson(prompt.prompt)}')">
                        Copy
                    </button>
                </div>
            </article>
        `).join('');
    }

    function renderPagination(items) {
        const container = document.getElementById('pagination');
        if (!container) return;

        const totalPages = Math.ceil(items.length / ITEMS_PER_PAGE);
        if (totalPages <= 1) {
            container.innerHTML = '';
            return;
        }

        let html = '';

        // Prev
        if (currentPage > 1) {
            html += `<button onclick="changePage(${currentPage - 1})" class="page-btn">&lt;</button>`;
        } else {
            html += `<button disabled class="page-btn">&lt;</button>`;
        }

        // Pages
        // Simple pagination: show all or max 5? Let's show all for now as list isn't huge yet (100 items = 5 pages)
        for (let i = 1; i <= totalPages; i++) {
            const activeClass = i === currentPage ? 'active' : '';
            html += `<button onclick="changePage(${i})" class="page-btn ${activeClass}">${i}</button>`;
        }

        // Next
        if (currentPage < totalPages) {
            html += `<button onclick="changePage(${currentPage + 1})" class="page-btn">&gt;</button>`;
        } else {
            html += `<button disabled class="page-btn">&gt;</button>`;
        }

        container.innerHTML = html;
    }

    // Utility to prevent XSS
    function escapeHtml(unsafe) {
        if (!unsafe) return '';
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    // Utility for safely putting string in onclick
    function escapeJson(str) {
        if (!str) return '';
        return str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '&quot;');
    }

    // Expose changePage to global scope for button onclicks
    window.changePage = (page) => {
        const urlParams = new URLSearchParams(window.location.search);
        urlParams.set('page', page);
        window.location.search = urlParams.toString();
    };
});

window.copyToClipboard = async (btn, text) => {
    try {
        await navigator.clipboard.writeText(text);
        const originalText = btn.textContent;
        btn.textContent = 'Copied!';
        btn.style.background = '#ffffff';
        btn.style.color = '#0d0d0d';

        setTimeout(() => {
            btn.textContent = originalText;
            btn.style.background = '';
            btn.style.color = '';
        }, 2000);
    } catch (err) {
        console.error('Failed to copy!', err);
        btn.textContent = 'Error';
    }
};
