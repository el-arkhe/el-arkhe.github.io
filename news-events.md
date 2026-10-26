---
layout: default
title: News & Events
permalink: /news-events/
nav_exclude: true
---

<div class="arkhe-events-page">

<div class="arkhe-events-page" markdown="1">
{% include arkhe-commercial-header.html %}

<h1>News & Events</h1>

<p>Explore courses, workshops, webinars, and scientific activities from Arkhe Multiomics.</p>

{% assign today = site.time | date: "%Y-%m-%d" %}
{% assign upcoming_events = site.events | sort: "date" %}
{% assign past_events = site.events | sort: "date" | reverse %}

<h2>Upcoming Events</h2>

<div class="arkhe-events-grid">
{% assign upcoming_count = 0 %}
{% for event in upcoming_events %}
  {% assign end_date = event.end_date | default: event.date | date: "%Y-%m-%d" %}
  {% if end_date >= today %}
    {% assign upcoming_count = upcoming_count | plus: 1 %}
    <article class="arkhe-event-card">
      <div class="arkhe-event-content">
        <p class="arkhe-eyebrow">{{ event.category | escape }} · {{ event.date | date: "%b %d, %Y" }}</p>
        <h3>{{ event.title | escape }}</h3>
        {% if event.collaborator %}
          <p>In collaboration with {{ event.collaborator | escape }}</p>
        {% endif %}
        <p>{{ event.excerpt | strip_html | truncatewords: 30 }}</p>
        <p><strong>{{ event.time | escape }}</strong></p>
        {% if event.registration_status == "open" %}
          <p>Registration Open</p>
        {% else %}
          <p>Upcoming</p>
        {% endif %}
        <a class="arkhe-textlink" href="{{ event.url | relative_url }}">Explore event →</a>
        {% if event.registration_status == "open" and event.registration_url != empty and event.registration_url != nil %}
          <a class="arkhe-textlink" href="{{ event.registration_url }}" target="_blank" rel="noopener noreferrer">Register now →</a>
        {% endif %}
      </div>
    </article>
  {% endif %}
{% endfor %}
</div>

{% if upcoming_count == 0 %}
<p>New activities will be announced soon.</p>
{% endif %}

<h2>Past Events</h2>

<div class="arkhe-events-grid">
{% assign past_count = 0 %}
{% for event in past_events %}
  {% assign end_date = event.end_date | default: event.date | date: "%Y-%m-%d" %}
  {% if end_date < today %}
    {% assign past_count = past_count | plus: 1 %}
    <article class="arkhe-event-card">
      <div class="arkhe-event-content">
        <p class="arkhe-eyebrow">{{ event.category | escape }} · {{ event.date | date: "%b %d, %Y" }}</p>
        <h3>{{ event.title | escape }}</h3>
        {% if event.collaborator %}
          <p>In collaboration with {{ event.collaborator | escape }}</p>
        {% endif %}
        <p>{{ event.excerpt | strip_html | truncatewords: 30 }}</p>
        <p><strong>{{ event.time | escape }}</strong></p>
        <a class="arkhe-textlink" href="{{ event.url | relative_url }}">Explore event →</a>
      </div>
    </article>
  {% endif %}
{% endfor %}
</div>

{% if past_count == 0 %}
<p>No past events to display.</p>
{% endif %}

</div>
