(function () {
  const nav = document.querySelector("[data-nav]");
  const menuBtn = document.querySelector("[data-menu]");
  const panel = document.querySelector("[data-panel]");
  const searchBtn = document.querySelector("[data-search]");
  const searchOverlay = document.querySelector("[data-search-overlay]");
  const searchInput = document.querySelector("[data-search-input]");
  const searchHits = document.querySelector("[data-search-hits]");
  const closeSearch = document.querySelector("[data-close-search]");

  const pages = [
    { t: "Home", u: "index.html" },
    { t: "PulseMind", u: "products/pulsemind.html" },
    { t: "PulseFlow", u: "products/pulseflow.html" },
    { t: "PulseCloud", u: "products/pulsecloud.html" },
    { t: "PulseSecure", u: "products/pulsesecure.html" },
    { t: "PulseInsight", u: "products/pulseinsight.html" },
    { t: "PulseConnect", u: "products/pulseconnect.html" },
    { t: "Enterprise AI", u: "solutions/enterprise.html" },
    { t: "Healthcare", u: "solutions/healthcare.html" },
    { t: "Financial Services", u: "solutions/finance.html" },
    { t: "Retail & Commerce", u: "solutions/retail.html" },
    { t: "Public Sector", u: "solutions/government.html" },
    { t: "Education", u: "solutions/education.html" },
    { t: "Features", u: "features.html" },
    { t: "Customers", u: "customers.html" },
    { t: "About", u: "about.html" },
    { t: "Contact", u: "contact.html" },
    { t: "Brand", u: "branding.html" },
    { t: "Sitemap", u: "sitemap.html" }
  ];

  const depth = Number(document.body.dataset.depth || "0");
  const prefix = depth > 0 ? "../".repeat(depth) : "";

  function abs(path) {
    if (path.startsWith("http") || path.startsWith("#")) return path;
    return prefix + path.replace(/^\//, "");
  }

  if (nav) {
    const onScroll = () => {
      nav.classList.toggle("scrolled", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  if (menuBtn && panel) {
    menuBtn.addEventListener("click", () => {
      const open = !panel.classList.contains("is-open");
      panel.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.setAttribute("aria-label", open ? "Close menu" : "Menu");
    });
  }

  function toggleSearch(open) {
    if (!searchOverlay) return;
    searchOverlay.classList.toggle("is-open", open);
    searchOverlay.setAttribute("aria-hidden", String(!open));
    document.body.classList.toggle("nav-open", open);
    if (open) {
      setTimeout(() => searchInput && searchInput.focus(), 40);
    }
  }

  if (searchBtn) searchBtn.addEventListener("click", () => toggleSearch(true));
  if (closeSearch) closeSearch.addEventListener("click", () => toggleSearch(false));
  if (searchOverlay) {
    searchOverlay.addEventListener("click", (e) => {
      if (e.target === searchOverlay) toggleSearch(false);
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      toggleSearch(false);
      if (panel) {
        panel.classList.remove("is-open");
        document.body.classList.remove("nav-open");
      }
    }
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      toggleSearch(true);
    }
  });

  if (searchInput && searchHits) {
    const render = (q) => {
      const query = q.trim().toLowerCase();
      const hits = pages.filter((p) => p.t.toLowerCase().includes(query)).slice(0, 8);
      searchHits.innerHTML = hits
        .map((p) => `<a href="${abs(p.u)}">${p.t}</a>`)
        .join("");
    };
    render("");
    searchInput.addEventListener("input", () => render(searchInput.value));
  }

  document.querySelectorAll("[data-accordion] h3").forEach((h) => {
    h.addEventListener("click", () => {
      if (window.matchMedia("(min-width: 834px)").matches) return;
      h.parentElement.classList.toggle("is-open");
    });
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.16, rootMargin: "0px 0px -8% 0px" }
  );
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  const form = document.querySelector("[data-contact-form]");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const required = ["name", "email", "message"];
      let ok = true;
      required.forEach((name) => {
        const el = form.querySelector(`[name="${name}"]`);
        if (!String(data.get(name) || "").trim()) {
          ok = false;
          el.style.borderColor = "#ff453a";
        } else {
          el.style.borderColor = "";
        }
      });
      const email = String(data.get("email") || "");
      if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        ok = false;
        form.querySelector('[name="email"]').style.borderColor = "#ff453a";
      }
      if (!ok) return;
      form.reset();
      const success = document.querySelector("[data-form-success]");
      if (success) success.classList.add("is-on");
    });
  }

  const params = new URLSearchParams(window.location.search);
  if (params.get("q") && searchInput) {
    toggleSearch(true);
    searchInput.value = params.get("q");
    searchInput.dispatchEvent(new Event("input"));
  }

  const year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
