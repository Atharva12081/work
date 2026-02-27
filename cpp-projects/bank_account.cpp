/*
 * File: bank_account.cpp
 * Description: Bank account management system using inheritance and polymorphism
 * Author: Atharva
 * Date: 2025-02-20
 */

#include <iostream>
#include <string>
#include <vector>
#include <ctime>

using namespace std;

// Base Account class
class Account {
protected:
    string accountNumber;
    string holderName;
    double balance;
    static int accountCounter;

public:
    Account(string name = "", double initialBalance = 0.0) 
        : holderName(name), balance(initialBalance) {
        accountNumber = generateAccountNumber();
    }

    virtual ~Account() {}

    string generateAccountNumber() {
        accountCounter++;
        return "ACC" + to_string(1000 + accountCounter);
    }

    virtual void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: $" << amount << endl;
        } else {
            cout << "Invalid deposit amount!" << endl;
        }
    }

    virtual bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            cout << "Withdrawn: $" << amount << endl;
            return true;
        } else {
            cout << "Insufficient balance or invalid amount!" << endl;
            return false;
        }
    }

    virtual void displayBalance() const {
        cout << "Account Number: " << accountNumber << endl;
        cout << "Holder Name: " << holderName << endl;
        cout << "Current Balance: $" << balance << endl;
    }

    string getAccountNumber() const { return accountNumber; }
    string getHolderName() const { return holderName; }
    double getBalance() const { return balance; }

    virtual double calculateInterest() const {
        return 0.0;
    }
};

int Account::accountCounter = 0;

// Savings Account class
class SavingsAccount : public Account {
private:
    double interestRate;
    double minimumBalance;

public:
    SavingsAccount(string name, double balance, double rate = 0.03) 
        : Account(name, balance), interestRate(rate), minimumBalance(100.0) {}

    double calculateInterest() const override {
        return balance * interestRate;
    }

    bool withdraw(double amount) override {
        if (balance - amount >= minimumBalance) {
            return Account::withdraw(amount);
        }
        cout << "Cannot withdraw! Minimum balance of $" 
             << minimumBalance << " required." << endl;
        return false;
    }

    void displayBalance() const override {
        Account::displayBalance();
        cout << "Account Type: Savings" << endl;
        cout << "Interest Rate: " << (interestRate * 100) << "%" << endl;
        cout << "Estimated Interest: $" << calculateInterest() << endl;
    }
};

// Checking Account class
class CheckingAccount : public Account {
private:
    double overdraftLimit;
    double overdraftUsed;

public:
    CheckingAccount(string name, double balance, double overdraft = 500.0)
        : Account(name, balance), overdraftLimit(overdraft), overdraftUsed(0.0) {}

    bool withdraw(double amount) override {
        if (amount > 0) {
            if (balance >= amount) {
                balance -= amount;
                cout << "Withdrawn: $" << amount << endl;
                return true;
            } else {
                double overdraftNeeded = amount - balance;
                if (overdraftNeeded <= (overdraftLimit - overdraftUsed)) {
                    balance = 0;
                    overdraftUsed += overdraftNeeded;
                    cout << "Withdrawn: $" << amount << " (using overdraft)" << endl;
                    return true;
                } else {
                    cout << "Insufficient funds!" << endl;
                    return false;
                }
            }
        }
        cout << "Invalid amount!" << endl;
        return false;
    }

    double calculateInterest() const override {
        return 0.0;
    }

    void displayBalance() const override {
        Account::displayBalance();
        cout << "Account Type: Checking" << endl;
        cout << "Overdraft Limit: $" << overdraftLimit << endl;
        cout << "Overdraft Used: $" << overdraftUsed << endl;
    }
};

// Bank class to manage accounts
class Bank {
private:
    vector<Account*> accounts;

public:
    ~Bank() {
        for (auto account : accounts) {
            delete account;
        }
    }

    void createAccount(string type, string name, double balance) {
        Account* newAccount = nullptr;
        
        if (type == "savings") {
            newAccount = new SavingsAccount(name, balance);
        } else if (type == "checking") {
            newAccount = new CheckingAccount(name, balance);
        } else {
            cout << "Invalid account type!" << endl;
            return;
        }
        
        accounts.push_back(newAccount);
        cout << "Account created successfully!" << endl;
        newAccount->displayBalance();
    }

    Account* findAccount(string accountNumber) {
        for (auto account : accounts) {
            if (account->getAccountNumber() == accountNumber) {
                return account;
            }
        }
        return nullptr;
    }

    void displayAllAccounts() const {
        cout << "\n===== All Accounts =====" << endl;
        for (const auto& account : accounts) {
            account->displayBalance();
            cout << "------------------------" << endl;
        }
    }

    int getAccountCount() const { return accounts.size(); }
};

int main() {
    Bank bank;

    // Create different types of accounts
    bank.createAccount("savings", "John Doe", 5000.0);
    bank.createAccount("checking", "Jane Smith", 3000.0);
    bank.createAccount("savings", "Bob Johnson", 10000.0);

    // Find and use an account
    Account* acc = bank.findAccount("ACC1001");
    if (acc) {
        acc->deposit(1000.0);
        acc->withdraw(500.0);
        acc->displayBalance();
    }

    bank.displayAllAccounts();

    return 0;
}

