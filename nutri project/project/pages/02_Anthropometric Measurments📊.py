import streamlit as st

def calculate_bmi(weight, height_cm):
    # Convert height from cm to meters
    height_m = height_cm / 100
    # BMI formula: weight (kg) / (height (m))^2
    bmi = weight / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0)
    height_cm = st.number_input("Enter your height (cm)", min_value=1.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height_cm)
        st.write(f"Your BMI is: {bmi:.2f}")
        interpretation = interpret_bmi(bmi)
        st.write(f"Interpretation: {interpretation}")

        # Visualization
        st.markdown("### BMI Meter")
        st.progress(bmi / 40.0)

if __name__ == "__main__":
    main()
