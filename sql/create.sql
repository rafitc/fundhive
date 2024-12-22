CREATE SCHEMA public 

-- Create users table
CREATE TABLE public.users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create fund families
CREATE TABLE fund_families (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- For first insert the values 
INSERT INTO fund_families (name) VALUES
    ('Aditya Birla Sun Life Mutual Fund'),
    ('Axis Mutual Fund'),
    ('Bajaj Finserv Mutual Fund'),
    ('Bandhan Mutual Fund'),
    ('Baroda BNP Paribas Mutual Fund'),
    ('Canara Robeco Mutual Fund'),
    ('DSP Mutual Fund'),
    ('Franklin Templeton Mutual Fund'),
    ('HDFC Mutual Fund'),
    ('HSBC Mutual Fund'),
    ('ICICI Prudential Mutual Fund'),
    ('Invesco Mutual Fund'),
    ('ITI Mutual Fund'),
    ('Kotak Mahindra Mutual Fund'),
    ('LIC Mutual Fund'),
    ('Mirae Asset Mutual Fund'),
    ('Nippon India Mutual Fund'),
    ('SBI Mutual Fund'),
    ('Sundaram Mutual Fund'),
    ('Trust Mutual Fund'),
    ('UTI Mutual Fund'),
    ('PGIM India Mutual Fund'),
    ('Tata Mutual Fund'),
    ('Union Mutual Fund'),
    ('Bank of India Mutual Fund'),
    ('360 ONE Mutual Fund (Formerly Known as IIFL Mutual Fund)'),
    ('Groww Mutual Fund'),
    ('JM Financial Mutual Fund'),
    ('Mahindra Manulife Mutual Fund'),
    ('Quantum Mutual Fund'),
    ('quant Mutual Fund'),
    ('Edelweiss Mutual Fund'),
    ('Motilal Oswal Mutual Fund'),
    ('Navi Mutual Fund'),
    ('PPFAS Mutual Fund'),
    ('WhiteOak Capital Mutual Fund'),
    ('Helios Mutual Fund'),
    ('NJ Mutual Fund'),
    ('Samco Mutual Fund'),
    ('Shriram Mutual Fund'),
    ('Taurus Mutual Fund'),
    ('Zerodha Mutual Fund'),
    ('Old Bridge Mutual Fund');

-- Fund scheme 
CREATE TABLE public.mutual_fund_schemes (
    id serial PRIMARY KEY,  -- Add an id column as a serial type
    scheme_code int4 NOT NULL,
    isin_div_payout_isin_growth varchar(12) NOT NULL,
    isin_div_reinvestment varchar(12) NOT NULL,
    scheme_name varchar(255) NOT NULL,
    net_asset_value numeric(10, 4) NOT NULL,
    "date" date NOT NULL,
    scheme_type varchar(50) NOT NULL,
    scheme_category varchar(100) NOT NULL,
    fund_family_id int4 NULL,
    created_on timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    last_updated_on timestamp DEFAULT CURRENT_TIMESTAMP NULL
);

-- portfolio 
CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- portfolio mutual fund 
CREATE TABLE portfolio_mutual_funds (
    id SERIAL PRIMARY KEY,
    portfolio_id INT REFERENCES portfolios(id) ON DELETE CASCADE,
    mutual_fund_scheme_id INT REFERENCES mutual_fund_schemes(id) ON DELETE CASCADE,
    units DECIMAL(10, 2) NOT NULL, -- Number of units held
    purchase_price DECIMAL(10, 2) NOT NULL, -- Price at which units were bought
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- add unique code 
alter table mutual_fund_schemes 
add column scheme_code varchar(255);

