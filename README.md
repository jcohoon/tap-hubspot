# tap-hubspot

This is a [Singer](https://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:
- Pulls raw data from HubSpot's [REST API](http://developers.hubspot.com/docs/overview)
- Extracts the following resources from HubSpot
  - [Campaigns](http://developers.hubspot.com/docs/methods/email/get_campaign_data)
  - [Companies](http://developers.hubspot.com/docs/methods/companies/get_company)
  - [Contacts](https://developers.hubspot.com/docs/methods/contacts/get_contacts)
  - [Contact Lists](http://developers.hubspot.com/docs/methods/lists/get_lists)
  - [Deals](http://developers.hubspot.com/docs/methods/deals/get_deals_modified)
  - [Deal Pipelines](https://developers.hubspot.com/docs/methods/deal-pipelines/get-all-deal-pipelines)
  - [Email Events](http://developers.hubspot.com/docs/methods/email/get_events)
  - [Engagements](https://developers.hubspot.com/docs/methods/engagements/get-all-engagements)
  - [Forms](http://developers.hubspot.com/docs/methods/forms/v2/get_forms)
  - [Keywords](http://developers.hubspot.com/docs/methods/keywords/get_keywords)
  - [Owners](https://developers.hubspot.com/docs/api/crm/owners)
  - [Subscription Changes](http://developers.hubspot.com/docs/methods/email/get_subscriptions_timeline)
  - [Workflows](http://developers.hubspot.com/docs/methods/workflows/v3/get_workflows)
  - [Tickets](https://developers.hubspot.com/docs/api/crm/tickets)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## Configuration

This tap requires a `config.json` which specifies details regarding authentication, either via [OAuth 2.0](https://developers.hubspot.com/docs/methods/oauth2/oauth2-overview) or a Private App personal access token (PAT). It also includes a cutoff date for syncing historical data, an optional parameter `request_timeout` and a flag which controls collection of anonymous usage metrics. See [config.sample.json](config.sample.json) for an example. You may specify an API key instead of OAuth parameters for development purposes, as detailed below.

To run `tap-hubspot` with the configuration file, use this command:

```bash
› tap-hubspot -c my-config.json
```

### Private App PAT Authentication

To use a HubSpot Private App token, set `auth_method` to `pat` and provide your
token via the `access_token` field:

```json
{
  "auth_method": "pat",
  "access_token": "pat-123",
  "start_date": "2023-01-01T00:00:00Z"
}
```

Environment variables such as `TAP_HUBSPOT_AUTH_METHOD` and
`TAP_HUBSPOT_ACCESS_TOKEN` may also be used in place of values in the config
file.


## API Key Authentication (for development)

As an alternative to OAuth 2.0 authentication during development, you may specify an API key (`HAPIKEY`) to authenticate with the HubSpot API. This should be used only for low-volume development work, as the [HubSpot API Usage Guidelines](https://developers.hubspot.com/apps/api_guidelines) specify that integrations should use OAuth for authentication.

To use an API key, include a `hapikey` configuration variable in your `config.json` and set it to the value of your HubSpot API key. Any OAuth authentication parameters in your `config.json` **will be ignored** if this key is present!

---

Copyright &copy; 2017 Stitch
