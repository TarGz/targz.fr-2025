module Jekyll
  class LlmsTxtPage < PageWithoutAFile
    def initialize(site, content)
      @site = site
      @base = site.source
      @dir  = ""
      @name = "llms.txt"
      self.process(@name)
      self.content = content
      self.data = { "layout" => nil }
    end
  end

  class LlmsTxtGenerator < Generator
    safe true
    priority :low

    def generate(site)
      # Remove static llms.txt if present so we don't get a conflict
      site.pages.delete_if { |p| p.name == "llms.txt" }

      content = build_content(site)
      site.pages << LlmsTxtPage.new(site, content)
    end

    private

    def clean_desc(text, max = 120)
      return "" if text.nil? || text.empty?
      # Strip markdown headings, links, newlines
      text = text.gsub(/#+\s+/, "").gsub(/\[([^\]]+)\]\([^)]+\)/, '\1').gsub(/\n+/, " ").strip
      text.length > max ? text[0, max].gsub(/\s+\S+$/, "") + "..." : text
    end

    def build_content(site)
      base_url = site.config["url"] || "https://targz.fr"

      exhibitions = site.posts.docs
        .select  { |p| p.data["category"] == "exhibitions" }
        .sort_by { |p| p.date }.reverse

      portfolio = site.posts.docs
        .select  { |p| p.data["category"] == "portfolio" }
        .sort_by { |p| p.date }.reverse

      commissions = site.posts.docs
        .select  { |p| p.data["category"] == "commissions" }
        .sort_by { |p| p.date }.reverse

      lines = []

      lines << "# Targz"
      lines << ""
      lines << "> Pen plotter and generative artist. Self-taught, geek-turned-artist. Creates algorithmic Op Art executed by precision pen plotters with archival inks on paper and canvas."
      lines << ""
      lines << "No art school, no engineering degree, no programming courses. Everything learned from the community and open source tools. My practice is driven by a weird ability to see things in abstract shapes (artefacts), akin to pareidolia. I build my own generative tools (JavaScript, Processing) and a custom pen plotter to bring them to life."
      lines << ""

      lines << "## Exhibitions"
      lines << ""
      exhibitions.each do |post|
        title = post.data["title"]
        url   = "#{base_url}#{post.url}"
        desc  = clean_desc(post.data["description"] || post.data["location"] || "")
        year  = post.date.year
        note  = [desc, year.to_s].reject(&:empty?).join(", ")
        lines << "- [#{title}](#{url})#{note.empty? ? "" : ": #{note}"}"
      end
      lines << ""

      lines << "## Portfolio"
      lines << ""
      lines << "- [Portfolio](#{base_url}/portfolio/): Full collection of pen plotter artworks"
      lines << "- [Bits](#{base_url}/bits/): Artistic explorations not related to pen plotting"
      lines << ""
      portfolio.first(15).each do |post|
        title = post.data["title"]
        url   = "#{base_url}#{post.url}"
        desc  = clean_desc(post.data["description"] || "")
        lines << "- [#{title}](#{url})#{desc.empty? ? "" : ": #{desc}"}"
      end
      lines << ""

      lines << "## Commissions"
      lines << ""
      lines << "- [Commissions](#{base_url}/commissions/): Custom pen plotter portraits, corporate art, bespoke generative pieces"
      commissions.each do |post|
        title = post.data["title"]
        url   = "#{base_url}#{post.url}"
        desc  = clean_desc(post.data["description"] || "")
        lines << "- [#{title}](#{url})#{desc.empty? ? "" : ": #{desc}"}"
      end
      lines << ""

      lines << "## Optional"
      lines << ""
      lines << "- [About](#{base_url}/about/): Full artist statement"
      lines << "- [Instagram](https://instagram.com/targz): Process videos and artwork"
      lines << "- [Reddit](https://www.reddit.com/user/_targz_/submitted/): Community posts"

      lines.join("\n")
    end
  end
end
