 # breakeeven.md

## Cost per Active User (CPU)

The cost per active user (CPU) for `scope-shield` is estimated as follows:

- Compute: $0.01 per active user per month (based on AWS EC2 t2.micro instance cost)
- Storage: $0.005 per active user per month (based on AWS S3 storage cost)
- Bandwidth: $0.001 per active user per month (based on AWS data transfer cost)

Total CPU: $0.016 per active user per month

## Pricing Tiers

We propose the following pricing tiers for `scope-shield`:

1. **Starter**: $5/month
   - Basic project management features
   - Limited user access (up to 5 users)
   - Email support

2. **Pro**: $15/month
   - Advanced project management features
   - Unlimited user access
   - Priority email support
   - Monthly project health report

3. **Enterprise**: Custom pricing (contact sales)
   - All Pro features
   - Dedicated account manager
   - Custom integrations
   - SLA-backed service level agreements

## Customer Acquisition Cost (CAC) and LTV Estimate

Based on market research and historical data, we estimate the following metrics for `scope-shield`:

- CAC: $150 (average cost to acquire a customer, including marketing and sales expenses)
- LTV (Lifetime Value): $600 (estimated value a customer brings to the company over their lifetime)

## Break-even Users Count

To break even, we need to reach a point where the total revenue from active users equals the total cost of acquiring those users.

Break-even users count: 9375 (total CAC / (CPU * ARPU))

Assuming an ARPU (Average Revenue Per User) of $10 (average revenue per user, considering the Starter and Pro tiers), the break-even point is reached when we have 9375 active users.

## Path to $10K MRR

To reach $10K MRR (Monthly Recurring Revenue), we need to find a way to acquire and retain 625 active users (assuming an ARPU of $10).

At the current pricing tiers, we can achieve this by focusing on the Pro tier, as it has a higher ARPU and offers more features that might attract open source project maintainers. To reach 625 Pro tier users, we can target open source communities, attend relevant conferences, and invest in targeted marketing campaigns.

By focusing on the Pro tier and optimizing our sales and marketing efforts, we can reach our goal of $10K MRR and continue to grow the `scope-shield` user base.