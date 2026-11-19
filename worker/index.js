// Cloudflare Worker in front of the static Hugo build in public/.
//
// Its only job is the www -> bare domain redirect that Netlify used to do.
// Every other request is handed to the static assets, which also apply
// public/_redirects (the /go/ affiliate links) and public/_headers.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
      url.protocol = "https:";
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
