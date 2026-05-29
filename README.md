# Frontend for HTTP Server

In Tuesday's class you built and debugged a low-level Python HTTP server ([HTTP Server 1](https://github.com/CP-Evenings-and-Weekends/http-server-1) and [HTTP Server 2](https://github.com/CP-Evenings-and-Weekends/http-server-2)).  Today you'll add a third endpoint, then write a browser frontend that talks to it.

Starter files are included: `server.py`, `index.html`, `app.js`, `style.css`.

## Requirements

### 1. Add a third endpoint to your server

Copy your working server code from HTTP Server 2 into `server.py`.  Then add a third route — pick something interesting that returns **JSON** (a list of quotes, fake products, a counter, anything).

### 2. Build a frontend that calls it

In `index.html` + `app.js`, build a page that:
- Has a button (or other input) that triggers a `fetch` call to your new endpoint
- Renders the response into the DOM using vanilla JS (no React yet)
- Uses Bootstrap (or other CSS framework) classes if you want, mirroring today's lesson

### 3. Handle the CORS error you'll hit

When the browser loads `index.html` (via `file://` or Live Server) and tries to `fetch` from `localhost:9292`, you'll see a [CORS error](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

**Do not install a browser extension to disable CORS.**  Instead, fix it where it belongs: in your server's response headers.

Send back at minimum:

```
Access-Control-Allow-Origin: *
```

…on every response (alongside your existing `Content-Type` and `Content-Length` headers).

### 4. Add a 3rd-party API

Wire in a second `fetch` to a public 3rd-party API (any of the ones from Monday's assignment — JSONPlaceholder, PokéAPI, etc.).  Use its data to enrich what your own endpoint returns (chain them, display both side by side, whatever you like).

## Things to think about
- Why does CORS exist at all?  What's it protecting against?
- The CORS error happens in the **browser**, not in `curl`.  Why does `curl http://localhost:9292/...` work fine while the same URL from `app.js` throws?
- Your endpoint sends `Content-Type: application/json`.  What happens if you send `text/html` instead — does the browser still let your JS read it?

## Stretch
- Add a `POST` endpoint to your server and a form on the frontend that posts to it.  You'll need to handle the request body in Python (look at `client_connection.recv(...)`).
- Send `Access-Control-Allow-Origin` with a specific origin (e.g. `http://localhost:5500`) instead of `*`, and make sure the page still works.
- Add a loading spinner that shows while the fetch is in flight.
- Move your CORS headers into a helper function so every endpoint stays clean.

> Stuck? Have a code error? Use the ["4 Before Me"](https://docs.google.com/document/d/1nseOs5oabYBKNHfwJZNAR7GlU0zkZxNagsw63AD7XV0/edit) debugging checklist to help you solve it!
